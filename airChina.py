from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from datetime import timedelta
import sys

url = 'https://www.airchina.co.uk/GB/CN/Search'

driver = webdriver.Chrome(executable_path='/Users/lizhanglin/Documents/Mentoring/PersonalProjects/selenium/chromedriver')
driver.implicitly_wait(20)
driver.get(url)

# driver.find_element_by_id('fromSource').send_keys('伦敦')
# time.sleep(20)
driver.find_element_by_id('FSB1ToDestination').send_keys('上海, PVG')
time.sleep(20)
# driver.find_element_by_xpath("//*[@id='flightSearch']/div[2]/form/div[3]/div[1]/div[2]/div/span[2]").click()

