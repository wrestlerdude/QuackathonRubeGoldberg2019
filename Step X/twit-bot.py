#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Key Libraries
import urllib2, time, getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

password = getpass.getpass("Please Input password: ")

# ChromeOptions variables
options = webdriver.ChromeOptions()
options.add_argument('window-size=0')
# options.set_headless(headless=True)
# options.add_argument("user-data-dir=C:/Users/migue/AppData/Local/Google/Chrome/User Data")

# Browser def.
browser = webdriver.Chrome(('chromedriver.exe'),chrome_options=options)

# Status Message
print('\n' + ' --------- Accessing into your Twitter m8 ---------' + '\n')

browser.get('https://twitter.com/login') # items spreadsheet

browser.find_element_by_xpath('.//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys("miguelbacharov@hotmail.com")
time.sleep(0.1)
# Miguel2000
browser.find_element_by_xpath('.//*[@id="page-container"]/div/div[1]/form/fieldset/div[2]/input').send_keys(password)
time.sleep(0.1)
browser.find_element_by_xpath('.//*[@id="page-container"]/div/div[1]/form/div[2]/button').send_keys(Keys.ENTER)


# Status Message
print('\n' + ' --------- Logged into your Twitter m8 ---------' + '\n')
