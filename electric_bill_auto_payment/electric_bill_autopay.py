from time import sleep
from selenium import webdriver
import configparser

config = configparser.ConfigParser()
#config file format should be like the below.  Phone # must follow below format
'''
[Electric_Bill]
username=someusername
password=somepassword
routing=somerouting
account=someaccount
bankName=someBankNameSpacesAllowed
accountName=FullNameOfAccountHolder
firstName=firstNameOfAccountHolder
lastName=lastNameOfAccountHolder
phone=(123)456-8888
email=someEmailAddress
'''
config.read("/usr/local/etc/python_config.txt")

# starting a new browser session
browser = webdriver.Chrome()

# navigating to a webpage
browser.get('https://www.starnik.net/UtilityTrakR/UT3/Current/R_Default.aspx')

#get elements and enter username and password to login
browser.find_element_by_name('ctl04$login$ctl00$txtUsername').send_keys(config.get("Electric_Bill","username"))
browser.find_element_by_name('ctl04$login$ctl00$txtPassword').send_keys(config.get("Electric_Bill","password"))

#click login button to login to the site.
browser.find_element_by_name("ctl04$login$ctl00$btnLogin").click()

#once logged in, click the Pay now button and that will bring up a new pop up to submit payment
browser.find_element_by_name('ctl04$Menu1$ctl00$btnPay').click()

#switch control to the popup window and thus the browser var has a reference to that dom.
browser.switch_to_window(browser.window_handles[1])

#browser.find_elements_by_css("input[type='radio'][value='rdoCheckingAccount']").click
browser.find_element_by_id('ctl04_ctl00_rdoCheckingAccount').click()
#give a little time for the click.  might not need it, but just so we don't get not found as the other elements come into visibility
sleep(1)
browser.find_element_by_name('ctl04$ctl00$txtBankName').send_keys(config.get("Electric_Bill","bankName"))
browser.find_element_by_name('ctl04$ctl00$txtAccountName').send_keys(config.get("Electric_Bill","accountName"))
browser.find_element_by_name('ctl04$ctl00$txtBillingFirstName').send_keys(config.get("Electric_Bill","firstName"))
browser.find_element_by_name('ctl04$ctl00$txtBillingLastName').send_keys(config.get("Electric_Bill","lastName"))
browser.find_element_by_id('ctl04_ctl00_chkSameAddress').click()
browser.find_element_by_name('ctl04$ctl00$txtBillingPhone').send_keys(config.get("Electric_Bill","phone"))
browser.find_element_by_name('ctl04$ctl00$txtEmail').send_keys(config.get("Electric_Bill","email"))
#routing
browser.find_element_by_name('ctl04$ctl00$txtABACode').send_keys(config.get("Electric_Bill","routing"))
browser.find_element_by_name('ctl04$ctl00$txtConfirmABACode').send_keys(config.get("Electric_Bill","routing"))

#acct num
browser.find_element_by_name('ctl04$ctl00$txtAccountNumber').send_keys(config.get("Electric_Bill","account"))
browser.find_element_by_name('ctl04$ctl00$txtConfirmAccountNumber').send_keys(config.get("Electric_Bill","account"))

#get the balance due from the form and populate the full balance due for what I will pay.
balance_due = browser.find_element_by_id('ctl04_ctl00_lblCheckCurrentBalance').text
browser.find_element_by_name('ctl04$ctl00$txtCheckAmount').send_keys(balance_due[1:])

#click continue
browser.find_element_by_name('ctl04$ctl00$btnSubmit').click()

#accepts the alert box popup.
browser.switch_to_alert().accept()

#click the i agree
browser.find_element_by_name('ctl04$ctl00$chkAgree').click()

#confirm the payment.  Sleep 30 seconds before doing so so that I can review.
sleep(30)
browser.find_element_by_name('ctl04$ctl00$btnConfirm').click()

#closes the popup.  Might need to get rid of this if I automate the confirm and the window closes as part of that.
browser.close()

#now switch back to the main window and log out and close the main window
browser.switch_to_window(browser.window_handles[0])

#log out
browser.find_element_by_id('menu2').click()

#close main window
browser.close()
