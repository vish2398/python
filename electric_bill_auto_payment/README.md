# Automating payment of my Electric Bill

My electric bill company does not support auto-pay (it's 2017!!!), and it also does not save form info that was filled out previously. There is a very
tedious form that needs to be filled out each month, which includes entering my bank account # and routing #, as well as other information.  I wanted to automate thistask.  In order to automate it, I have used Python 3 and Selenium.  Now, when it comes time to pay my electric bill each month, I just have to run this simple script and it takes seconds instead of several minutes.

## Getting Started
This can be modified for other uses, but currently my electric company is QuadLogic, and they use Starnik as their portal.

### Prerequisites
Just need a machine with:
Python3
selenium
configparser

You should also make sure you have Chromium in your PATH variable.  It can be downloaded here: https://sites.google.com/a/chromium.org/chromedriver/getting-started

I added ~/bin/chromedriver to my path
```
ex. pip3 install selenium, pip3 install configparser
```

## License

This project is licensed under the MIT License
