#!/usr/bin/python
# -*- coding: utf-8 -*-
# script to fix manageengine servicedesk mail retrieve problem
# by opening administrative page and clicking buttons to stop
# and start helpdesk mail
 
import codecs
import sys
import os
import time
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://ip/'

NEXT_BUTTON_XPATH = '//input[@type="submit" and @value=u"Вход"]'

# use firefox to get page with javascript generated content
with closing(Firefox()) as browser:
     browser.get(url)
     username = browser.find_element_by_id("username")
     password = browser.find_element_by_id("password")
     option = browser.find_element_by_id("optionMsg")
     # click options button
     option.click()
     # use Local Authentication
     select = browser.find_element_by_css_selector('select')
     options = browser.find_elements_by_css_selector('option')
     for option in options:
         if option.get_attribute('value') == u'Local Authentication':
             option.click()
     username.send_keys("login")
     password.send_keys("password")

#     button = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
     button = browser.find_element_by_name("loginButton")
     button.click()
     
     url='https://ip/SetUpWizard.do?forwardTo=email'
     browser.get(url)
     mailstopbutton = browser.find_element_by_name("submit")
     mailstopbutton.click()
     # pause 5 sec
     time.sleep(5)
     mailstopbutton = browser.find_element_by_name("submit")
     mailstopbutton.click()
