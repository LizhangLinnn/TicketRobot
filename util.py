from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from datetime import timedelta
import sys
import json

from bs4 import BeautifulSoup

def select_date(driver, inputElement, date):
    inputElement.click()
    # check current calendar selection range
    while True:
        left_prev_mark_element = driver.find_element_by_xpath("//div[@id='Jcal_group0']/div[@class='body']/div[@class='Jcal_head']/mark[@id='Prev']")
        left_start_date = left_prev_mark_element.get_attribute("data-value")
        right_next_mark_element = driver.find_element_by_xpath("//div[@id='Jcal_group1']/div[@class='body']/div[@class='Jcal_head']/mark[@id='Next']")
        right_end_date = right_next_mark_element.get_attribute("data-value")
        if date <= left_start_date:
            # go to prev mark
            left_prev_mark_element.click()
        elif date >= right_end_date:
            # go to next mark
            right_next_mark_element.click()
        else:
            driver.find_element_by_xpath("//div[@date='{}']".format(date)).click()
            print("selected")
            break

def select_city(driver, inputElement, city, country):
    inputElement.click()
    inputElement.clear()
    inputElement.send_keys(city)
    inputElement.click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//li[contains(., '{}') and contains(., '{}')]/span[1]".format(city, country)).click()

def search_flight(driver):
    driver.find_element_by_xpath("//button[@id='btn_flight_search']").click()

def check_if_flight_available(driver):
    driver.implicitly_wait(10)
    elements = driver.find_elements_by_xpath("//dd[contains(., '￥')]")
    for ele in elements:
        print(ele.get_attribute('innerHTML'))

# input is either 'Prev' or 'Next'
def xPathCalRange(input):
    return "//div[@id='Jcal_group0']/div[@class='body']/div[@class='Jcal_head']/mark[@id='{}']".format(input)

def to_url_date_format(input):
    return '20' + str(input.month).zfill(2) + str(input.day).zfill(2)

def write_ticket_to_file(is_return, line_to_write):
    file_name = "return_tickets.txt" if is_return else "depart_tickets.txt"
    f = open(file_name, "a")
    f.write(line_to_write)
    f.close()
    print(line_to_write)


per_route_ticket_details = {}


def load_ticket_search_page(driver, from_airport, to_airport, selected_date):
    while (True):
        driver.get("http://www.ceair.com/booking/{}-{}-20{}{}_CNY.html".format(from_airport,
                                                                               to_airport,
                                                                               str(
                                                                                   selected_date.month).zfill(
                                                                                   2),
                                                                               str(
                                                                                   selected_date.day).zfill(
                                                                                   2)))
        time.sleep(30)

        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc, 'html.parser')

        # check if the web page is blocked by verification popup
        if soup.find(id='geetest') is None or len(soup.find(id='geetest')) == 0:
            break

def user_login(driver):
#     username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='username']")))
#     username_input.sendKeys("330382199408310917")
#     password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
#     password_input.sendKeys("83191194")
#     driver.find_element_by_xpath("//input[@name='login']").click()
#     print("clicked on login button")
#     driver.get("http://www.ceair.com/")
#     time.sleep(60)
    None

def alarm():
    print("playing alarm")
    from playsound import playsound
    playsound('fire_alarm.wav')


def buy_ticket(driver):
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    economy_exist = soup.find('dd', {'class', 'price economy COMMON_SOTO'}) is not None
    print("economy_exist" + str(economy_exist))
    premium_economy_exist = soup.find('dd', {'class', 'price PremiumEconomy COMMON_SOTO'}) is not None
    print("premium_economy_exist" + str(premium_economy_exist))
    luxury_exist = soup.find('dd', {'class', 'price luxury COMMON_SOTO'}) is not None
    print("luxury_exist" + str(luxury_exist))
    if economy_exist is True:
        driver.find_element_by_xpath("//dd[@data-type='{}']".format('economy')).click()
        driver.find_element_by_xpath("//div[@data-type='{}']/dl/dd[@class='p-b']/button[@productcd='COMMON_SOTO']".format('economy')).click()

        print("clicked!!!!!====")
        # alarm myself
        alarm()

        time.sleep(3600)
    elif premium_economy_exist is True:
        driver.find_element_by_xpath("//dd[@data-type='{}']".format('PremiumEconomy')).click()
        driver.find_element_by_xpath("//div[@data-type='{}']/dl/dd[@class='p-b']/button[@productcd='COMMON_SOTO']".format('PremiumEconomy')).click()

        print("clicked!!!!!====")
        # alarm myself
        alarm()

        time.sleep(3600)
    elif luxury_exist is True:
        driver.find_element_by_xpath("//dd[@data-type='{}']".format('luxury')).click()
        driver.find_element_by_xpath("//div[@data-type='{}']/dl/dd[@class='p-b']/button[@productcd='COMMON_SOTO']".format('luxury')).click()

        print("clicked!!!!!====")
        # alarm myself
        alarm()

        time.sleep(3600)

def check_ticket_details_after_loading_page(driver, current_focused_date):
    # get the current available ticket details
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')

    # days_in_week_info = soup.find_all('li', {'data-odnumber': '0'})
    # for day_in_week_info in days_in_week_info:
    #     day_in_week_info = str(day_in_week_info.text)
    #     # is an available ticket
    #     if "点击查看" not in day_in_week_info:
    #         parts = day_in_week_info.split(' ')
    #         # get date
    #         ticket_date = parts[0]
    #         ticket_price = parts[3]
    #         date_parts = ticket_date.split('-')
    #         month = int(date_parts[0])
    #         day = int(date_parts[1])


    # check that the ticket is buyable
    ticket_detail_section = str(soup.find('section', {'class': 'detail'}).text)
    print(ticket_detail_section)
    # ticket is buyable
    if "￥" in ticket_detail_section:
        print(current_focused_date.__str__() + " " + ticket_detail_section)

        # click to buy ticket
        buy_ticket(driver)


def search_ticket_for_all_dates(driver, start_date, end_date, from_airport, to_airport, is_return):
    driver.set_page_load_timeout(30)

    current_focused_date = start_date

    key = from_airport + "-" + to_airport
    if key not in per_route_ticket_details:
        per_route_ticket_details[key] = {}

    try:
        while current_focused_date <= end_date:
            load_ticket_search_page(driver, from_airport, to_airport, current_focused_date)

            check_ticket_details_after_loading_page(driver, current_focused_date)

            # move on to next week
            current_focused_date = current_focused_date + timedelta(days=7)

        # # check new tickets being identified and previously detected tickets being sold
        # new_tickets = current_detected_tickets_dates - previously_detected_ticket_date_by_detection_time_map.keys()
        # sold_tickets = previously_detected_ticket_date_by_detection_time_map.keys() - current_detected_tickets_dates
        # print("new_tickets: {}".format(new_tickets))
        # print("sold_tickets: {}".format(sold_tickets))
        # # process new tickets
        # for new_ticket in new_tickets:
        #     # add to cache - record it's not a new ticket any more
        #     previously_detected_ticket_date_by_detection_time_map[new_ticket] = time.time()
        #
        #     # write to file
        #     line_to_write = "From {} to {}: \nDate: {}\n\n".format(from_airport, to_airport, new_ticket)
        #     write_ticket_to_file(is_return, line_to_write)
        # for sold_ticket in sold_tickets:
        #     line_to_write = "Ticket from {} to {} on {} was sold after {} seconds.\n".format(from_airport,
        #                                                                                      to_airport,
        #                                                                                      sold_ticket,
        #                                                                                      time.time() - previously_detected_ticket_date_by_detection_time_map[sold_ticket])
        #     # write to file
        #     file_name = "sold_tickets.txt"
        #     f = open(file_name, "a")
        #     f.write(line_to_write)
        #     f.close()
        #     print(line_to_write)
        #     del previously_detected_ticket_date_by_detection_time_map[sold_ticket]
    except:
        print(sys.exc_info()[0])



    # soup = BeautifulSoup(html_doc, 'html.parser')
    # tickets = soup.find_all("td", {'data-hasprice': '1'})
    #
    # # tell me how long it took for a ticket to be detected to when it's gone...
    # key = from_airport + '-' + to_airport
    # if key not in per_journey_detected_tickets_map:
    #     per_journey_detected_tickets_map[key] = {} # date -> timestamp in seconds
    #
    # curr_detected_ticket_dates = set()
    # prev_detected_ticket_and_detection_time = per_journey_detected_tickets_map.get(key)
    # prev_detected_ticket_dates = set(prev_detected_ticket_and_detection_time.keys())
    # for ticket in tickets:
    #     date = ticket.get("data-date")
    #     curr_detected_ticket_dates.add(date)
    #
    #     price = ticket.get("data-price")
    #     line_to_write = "From {} to {}: \nDate: {}\nPrice: {}\n\n".format(from_airport, to_airport, date, price)
    #
    #     # a new ticket being detected
    #     if date not in prev_detected_ticket_dates:
    #         write_ticket_to_file(is_return, line_to_write)
    #         prev_detected_ticket_and_detection_time[date] = time.time()
    #         prev_detected_ticket_dates.add(date)
    #
    # # tell me how long it took for a ticket to be detected to when it's gone...
    # # and remove gone tickets from the cache
    # sold_tickets = prev_detected_ticket_dates - curr_detected_ticket_dates
    # if len(sold_tickets) != 0:
    #     for sold_ticket in sold_tickets:
    #         time_gap_in_sec = time.time() - prev_detected_ticket_and_detection_time[sold_ticket]
    #         line_to_write = "{} ticket at date {} is recently sold in {} seconds\n\n".format(key, sold_ticket, time_gap_in_sec)
    #
    #         # write to file
    #         file_name = "sold_tickets.txt"
    #         f = open(file_name, "a")
    #         f.write(line_to_write)
    #         f.close()
    #
    #         # remove from cache
    #         del prev_detected_ticket_and_detection_time[sold_ticket]

def get_next_possible_flight_date(day_in_a_week_to_search):
    if day_in_a_week_to_search > date.today().day:
        start_date = date.today() + timedelta(days = 7 + date.today().day - day_in_a_week_to_search)
    elif day_in_a_week_to_search == date.today().day:
        start_date = date.today()
    else:
        start_date = date.today() + timedelta(days = 7 - date.today().day + day_in_a_week_to_search)

    if start_date < date.today() + timedelta(days = 7):
        start_date = start_date + timedelta(days = 7)
    return start_date

search_end_date = date(2020, 9, 15) # inclusive


def process_json_like_string_to_json(input):
    # remove substring before the first open curly bracket
    # remove substring after the last close curly bracket
    return input[input.find('{') : (input.rfind('}') + 1)]



def auth_header_json(token):
    return \
    json.dumps({
        'wl_deviceNoProvisioningRealm':
            {'ID':
                 {"app":
                      {"id": "AirChina",
                       "version": "1.0"},
                  "device":
                      {"environment": "iOS",
                       "id": "92706437-7FF4-4AA5-9003-D4E2949F87E7",
                       "os": "13.3.1",
                       "model": "iPhone"},
                  "custom": {},
                  "token": token}},
         "wl_authenticityRealm": "iUCxdUSstVXVyDl9bKy9RXUEAHlgrMyJbX11THnI="
    })

# day_in_a_week_to_search: index of the day in a week - e.g. 4 == Friday (index starting from 0)
def air_china_curl(curl_search_all_query_base, start, desti, day_in_a_week_to_search):
    import os

    if date.today().weekday() >= day_in_a_week_to_search:
        start_date = date.today() + timedelta(days = 14 - (date.today().weekday() - day_in_a_week_to_search))
    else:
        start_date = date.today() + timedelta(days = 7 + day_in_a_week_to_search - date.today().weekday())

    end_date = date(2020, 7, 17)
    dates_to_search = list() # in ISO format YYYY-MM-DD

    while start_date <= end_date:
        dates_to_search.append(start_date.isoformat())
        start_date += timedelta(days = 7)

    print("------dates to search is : {}".format(dates_to_search))


    while True:
        try :
            process = os.popen(curl_search_all_query_base)
            print("--------------------------------------")
            print("--------------------------------------")
            print("--------------------------------------")
            print("From {} to {}".format(start, desti))
            raw_output = process.read()
            output = json.loads(raw_output)['resp']
            process.close()

            # output is in the format of
            # {
            #     '2021-01-13': {'price': '3960', 'iszj': '0', 'date': '2021-01-13', 'type': '0', 'backDate': ''},
            #     '2021-01-14': {'price': '3970', 'iszj': '0', 'date': '2021-01-14', 'type': '0', 'backDate': ''}
            # }

            if len(raw_output) < 2000:
                print("====== output is =====: \n\n{}".format(output))
            else:
                print("output too long - suppress printing")

            # check if the dates we are interested in is available
            available_dates = list()
            for key in dates_to_search:
                if output[key]['price'] != '':
                    available_dates.append(output[key])

            if len(available_dates) != 0:
                print("FOUND FLIGHTS!!!!")
                print(available_dates)
                alarm()
                time.sleep(1800)
            time.sleep(30)
        except:
            print(sys.exc_info()[0])



def china_southern_curl(curl_base, start, desti):
    import os
    start_date = date(2020, 6, 18)
    end_date = date(2020, 8, 15)
    while True:
        time.sleep(2)

        date_to_query = start_date
        while date_to_query <= end_date:

            curl = curl_base.format(str(date_to_query.month).zfill(2), str(date_to_query.day).zfill(2))
            stream = os.popen(curl)
            output_in_json = json.load(str(stream.read()))

            print(date_to_query)
            print(output_in_json)
            date_to_query = date_to_query + timedelta(days=1)
        #
        # if "最低" in output:
        #     line_to_write = "Found! Date is {}".format(curls[i][0])
        #     print(line_to_write)
        #     if curls[i][0] < do_not_alarm_threshold:
        #         alarm()
        #     elif curls[i][0] < second_preference_threshold:
        #         file_name = "air-china-from-{}-to-{}.txt".format(start, desti)
        #         f = open(file_name, "a")
        #         f.write(line_to_write)
        #         f.close()
        #         print("Found ticket after the threshold - alarm suppressed - written to file {}".format(file_name))
        #     else:
        #         print("Found ticket after the threshold for second preference - do not write to file")
        # else:
        #     print("not found")
