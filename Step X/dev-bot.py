#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Key Libraries
import urllib2, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

user_name = input("Please input your user name: ")
password = input("Plase input your password: ")

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
print('\n' + ' --------- Accessing into your DevRant m8 ---------' + '\n')

browser.get('https://devrant.com/feed/top/month?login=1') # items spreadsheet

browser.find_element_by_xpath('.//*[@id="email"]').send_keys(user_name)
browser.find_element_by_xpath('.//*[@id="password"]').send_keys(password)
time.sleep(0.5)
# browser.find_element_by_xpath('.//*[@id="pass"]').send_keys(Keys.ENTER)
#
# # Status Message
# print('\n' + ' --------- Loged into your Facebook m8 ---------' + '\n')
#
# # Status Message
# print('\n' + ' --------- Locating string m8 ---------' + '\n')
