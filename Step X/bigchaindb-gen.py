#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Key Libraries
import urllib2, time, json, bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

string = raw_input("Please Input string: ")

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
print('\n' + ' --------- Accessing into BigchainDB m8 ---------' + '\n')

browser.get('https://www.bigchaindb.com/developers/getstarted/') # items spreadsheet
time.sleep(2)
browser.find_element_by_xpath('.//*[@id="message"]').send_keys(string)
browser.find_element_by_xpath('.//*[@id="message"]').send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath('.//*[@id="cookies-eu-accept"]').click()
time.sleep(2)
browser.find_element_by_xpath('./html/body/section/section[1]/div[1]/div/div[2]/div[3]/p[2]/a').click()
time.sleep(6)
