from selenium import webdriver
from util import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from datetime import timedelta
import sys

from bs4 import BeautifulSoup



def main():
    driver = webdriver.Chrome(executable_path='/Users/lizhanglin/Documents/Mentoring/PersonalProjects/selenium/chromedriver')
    driver.implicitly_wait(15)
    depart_end_date = date(2020, 7, 15)
    return_start_date = date(2020, 7, 26)
    return_end_date = date(2020, 8, 15)
    user_login(driver)

    while True:
        time.sleep(5)

        # Frankford (FRA) -> Shanghai (SHA)
        from_airport = "fra"
        to_airport = "sha"
        depart_start_date = date(2020, 6, 23) # Tuesday
        search_ticket_for_all_dates(driver, depart_start_date, depart_end_date, from_airport, to_airport, False)
        # search_ticket_for_all_dates(driver, return_start_date, return_end_date, to_airport, from_airport, True)

main()