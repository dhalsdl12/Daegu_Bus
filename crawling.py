from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time, sys, os


def stations(busstation):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    driver.get("https://businfo.daegu.go.kr/")

    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/iframe'))
    station_name = driver.find_element(By.XPATH, '//*[@id="searchTxt"]')
    station_name.send_keys(busstation)
    station_name.send_keys(Keys.RETURN)
    time.sleep(0.5)

    arr = []
    station_list = driver.find_elements(By.XPATH, '//*[@id="bsList"]/ul/li')
    for i in range(len(station_list)):
        if i == 5:
            button = driver.find_element(By.XPATH, '//*[@id="bsList"]/a')
            button.click()
            time.sleep(0.5)
        station_name = station_list[i].find_element(By.XPATH, './a/div[1]/h6')
        # print(str(i + 1) + ' : ' + station_name.text)
        arr.append((i + 1, station_name.text))
    
    driver.close()
    
    return arr


def busses(num, msg):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    driver.get("https://businfo.daegu.go.kr/")

    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/iframe'))
    station_name = driver.find_element(By.XPATH, '//*[@id="searchTxt"]')
    station_name.send_keys(msg)
    station_name.send_keys(Keys.RETURN)
    time.sleep(0.5)

    station = 'selectBS' + str(num)
    station_button = driver.find_element(By.XPATH, '//*[@id="' + station + '"]/a/div[1]/h6')
    # station_button.click()
    # click() 안될때 해결책
    station_button.send_keys(Keys.ENTER)
    time.sleep(1)

    number = []
    location = []
    bus_list = driver.find_elements(By.XPATH, '//*[@id="selectRouteList"]/ul/li')
    for bus in bus_list:
        bus_number = bus.find_element(By.XPATH, './div/a/div/h6').text
        bus_location = bus.find_element(By.XPATH, './ul/li[1]/div[1]/div/div').text
        bus_time = bus.find_element(By.XPATH, './ul/li[1]/div[3]/span').text

        if bus_time == '전' or bus_time == '전전':
            if bus_number[0].isdigit():
                number.append(bus_number + '       ' + bus_time)
                location.append(bus_location)
            else:
                number.append(bus_number + '     ' + bus_time)
                location.append(bus_location)
        elif bus_time != '':
            if int(bus_time[:-1]) <= 5:
                if bus_number[0].isdigit():
                    number.append(bus_number + '       ' + bus_time)
                    location.append(bus_location)
                else:
                    number.append(bus_number + '     ' + bus_time)
                    location.append(bus_location)
            else:
                break
    return number, location