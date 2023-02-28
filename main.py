from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time, sys, os


# pip install pyinstaller
# pyinstaller -F --add-binary "chromedriver.exe;." main.py
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome('chromedriver')


# driver 실행
driver.get("https://businfo.daegu.go.kr/")


busstation = input('[정류소, 노선, 목적지]를 입력하세요 : ')

# iframe으로 감싸져 있을때 해결책
driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/iframe'))
station_name = driver.find_element(By.XPATH, '//*[@id="searchTxt"]')
station_name.send_keys(busstation)
station_name.send_keys(Keys.RETURN)


station_list = driver.find_elements(By.XPATH, '//*[@id="bsList"]/ul')

for station in station_list:
    print('check')