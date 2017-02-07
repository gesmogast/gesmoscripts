#!/usr/bin/python
import codecs
import sys
import os
from contextlib import closing
from selenium.webdriver import Firefox # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait

name_list = ['p12Value','p15Value','p22Value','p5Value','p25Value','p18Value','p28Value','p29Value','p36Value','p37Value','p51Value','p50Value','p44Value','p47Value','p19Value','p64Value','p63Value','p68Value','p67Value']
mean_list = ['p12Name','p15Name','p22Name','p5Name','p25Name','p18Name','p28Name','p29Name','p36Name','p37Name','p51Name','p50Name','p44Name','p47Name','p19Name','p64Name','p63Name','p68Name','p67Name']
url = 'http://ip:8088/login.htm'

NEXT_BUTTON_XPATH = '//input[@type="submit" and @value="Login"]'

# use firefox to get page with javascript generated content
with closing(Firefox()) as browser:
     browser.get(url)
     username = browser.find_element_by_id("username")
     password = browser.find_element_by_id("password")

     username.send_keys("admin")
     password.send_keys("password")

     button = browser.find_element_by_xpath(NEXT_BUTTON_XPATH)
     button.click()
   # wait for the page to load
     WebDriverWait(browser, timeout=10).until(
         lambda x: x.find_element_by_id('p12Value'))
    # make 2 lists, sensor values and sensor names
     value_list = []
     meaning_list = []
    # iterate lists to obtain values and names from web page
     for value in name_list:
          value_list.append(browser.find_element_by_id(value).text)
     for value in mean_list:
          meaning_list.append(browser.find_element_by_id(value).text)
    # change encoding in order to write utf8 strings to file
     UTF8Writer = codecs.getwriter('utf8')
     sys.stdout = UTF8Writer(sys.stdout)
    # write lists to file ebro_output.txt
     f = open('ebro_output.txt', 'w')
     for (p,k) in zip(value_list,meaning_list):
          str = ''
          str = p + ' ' + k+'\n'
          encode_string = str.encode("utf8")
          f.write(encode_string)
     f.close()
    # copy this output file to remote zabbix system with scp
     os.system("scp /home/ebro_output.txt root@ip:/home/ebro/ebro_output.txt")
