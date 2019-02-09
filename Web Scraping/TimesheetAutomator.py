import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import re
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/niraj/Downloads/chromedriver_win32/chromedriver.exe')
ua = UserAgent()
header = { 'user-agent' : ua.chrome }

driver.get('https://compass.esa.cognizant.com/psp/ESA89PRD/?cmd=start')

uname = driver.find_element_by_id('username')
pwd = driver.find_element_by_id('PasswordInternal')

# time.sleep(20)
uname.send_keys(input("input(enter ID"))
pwd.send_keys(input("Enter PW"))

uname.submit()
time.sleep(10)

timesheet = driver.find_element_by_id("PS_EX_TIME_RPT_L_FL$0")
timesheet.click()

latesttimesheet = driver.find_element_by_id("CTS_TS_LAND_PER_DESCR30$0")
latesttimesheet.click()

time.sleep(20)
print("Hello")

saturday = driver.find_element_by_id("TIME1$0")
saturday.send_keys(input("Enter hours for saturday"))

sunday=driver.find_element_by_id("TIME2$0")
sunday.send_keys(input("sunday?"))

monday=driver.find_element_by_id("TIME3$0")
monday.send_keys(input("Monday?"))

tuesday=driver.find_element_by_id("TIME4$0")
tuesday.send_keys(input("Tuesday?"))

wednesday=driver.find_element_by_id("TIME5$0")
wednesday.send_keys(input("wednesday??"))

thursday=driver.find_element_by_id("TIME6$0")
thursday.send_keys(input("Thursday?"))

friday=driver.find_element_by_id("TIME7$0")
friday.send_keys(input("Friday?"))

friday.submit()
print("Hello")
time.sleep()
driver.close()













# except:
# 	print("cant fetch data, inform author")