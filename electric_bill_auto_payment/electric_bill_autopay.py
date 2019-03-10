from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
browser.find_element_by_name('ctl04$ctl00$txtUserName').send_keys(config.get("Electric_Bill","username"))
browser.find_element_by_name('ctl04$ctl00$txtPassword').send_keys(config.get("Electric_Bill","password"))

#click login button to login to the site.
browser.find_element_by_name("ctl04$ctl00$btnLogin").click()

#navigate to the pay bill link
browser.get('https://www.starnik.net/UtilityTrakR/UT3/Current/RP_PayBill.aspx');

#click continue on the payment summary
browser.find_element_by_name('ctl04$ctl01$btnSelectAccount').click()

#click on ECheck
browser.find_element_by_id('ctl04_ctl01_rblOnlinePaymentTypeGroupID_1').click()

browser.find_element_by_name('ctl04$ctl01$txtBankName').send_keys(config.get("Electric_Bill","bankName"))
browser.find_element_by_name('ctl04$ctl01$txtAccountName').send_keys(config.get("Electric_Bill","accountName"))

#routing number and confirm routing number
browser.find_element_by_name('ctl04$ctl01$txtABACode').send_keys(config.get("Electric_Bill","routing"))
browser.find_element_by_name('ctl04$ctl01$txtConfirmABACode').send_keys(config.get("Electric_Bill","routing"))

#acct num
browser.find_element_by_name('ctl04$ctl01$txtAccountNumber').send_keys(config.get("Electric_Bill","account"))
browser.find_element_by_name('ctl04$ctl01$txtConfirmAccountNumber').send_keys(config.get("Electric_Bill","account"))

browser.find_element_by_name('ctl04$ctl01$txtBillingFirstName').send_keys(config.get("Electric_Bill","firstName"))
browser.find_element_by_name('ctl04$ctl01$txtBillingLastName').send_keys(config.get("Electric_Bill","lastName"))


#street address
browser.find_element_by_name('ctl04$ctl01$txtBillingAddress').send_keys(config.get("Electric_Bill","streetAddress"))
browser.find_element_by_name('ctl04$ctl01$txtBillingCity').send_keys(config.get("Electric_Bill","city"))

stateSelect = Select(browser.find_element_by_id("ctl04_ctl01_ddlBillingStateID"))
stateSelect.select_by_value(config.get("Electric_Bill","state"))

browser.find_element_by_name('ctl04$ctl01$txtBillingZipCode').send_keys(config.get("Electric_Bill","zip"))


#click continue
browser.find_element_by_name('ctl04$ctl01$btnSubmit').click()

#accepts the alert box popup.
browser.switch_to_alert().accept()

#click the i agree
browser.find_element_by_name('ctl04$ctl01$chkAgree').click()

#confirm the payment.  Sleep 30 seconds before doing so so that I can review.
sleep(15)
browser.find_element_by_name('ctl04$ctl01$btnConfirm').click()

#accepts the alert box popup.
browser.switch_to_alert().accept()

#closes the popup.  Might need to get rid of this if I automate the confirm and the window closes as part of that.
#browser.close()

#now switch back to the main window and log out and close the main window
#browser.switch_to_window(browser.window_handles[0])

#review 
sleep(10)

#log out
browser.find_element_by_id('ctl04$ctl00$btnLogout').click()

#close main window
browser.close()
