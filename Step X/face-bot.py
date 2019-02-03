#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Key Libraries
import urllib2, time, getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

password = getpass.getpass("Please Input password: ")

# Timer
start_time = time.time()

# ChromeOptions variables
options = webdriver.ChromeOptions()
options.add_argument('window-size=0')
# options.set_headless(headless=True)
# options.add_argument("user-data-dir=C:/Users/migue/AppData/Local/Google/Chrome/User Data")

# Browser def.
browser = webdriver.Chrome(('chromedriver.exe'),chrome_options=options)

# Status Message
print('\n' + ' --------- Accessing into your Facebook m8 ---------' + '\n')

browser.get('https://facebook.com') # items spreadsheet

browser.find_element_by_xpath('.//*[@id="email"]').send_keys("miguelbacharov@hotmail.com")
# Miguel2000
browser.find_element_by_xpath('.//*[@id="pass"]').send_keys(password)
time.sleep(0.5)
browser.find_element_by_xpath('.//*[@id="pass"]').send_keys(Keys.ENTER)

# Status Message
print('\n' + ' --------- Loged into your Facebook m8 ---------' + '\n')

# Status Message
print('\n' + ' --------- Locating string m8 ---------' + '\n')



# html = browser.page_source

# END
# browser.quit()
