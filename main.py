import os
import time
import schedule
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


c1 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]'
c2 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]'
c3 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]'
c4 = '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]'


def onehr(var1):
    os.environ['PATH'] += r"C:/SeleniumDriver"
    driver = webdriver.Chrome()
    act = ActionChains(driver)
    WebDriverWait(driver, 10)
    driver.get("https://myclass.lpu.in/")
    driver.maximize_window()
    driver.find_element(By.NAME, 'i').send_keys(12111097)
    driver.find_element(
        By.CSS_SELECTOR, 'input[type="password"]').send_keys('December@1612')
    WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(driver, 2)
    driver.find_element(
        By.XPATH, '//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()
    WebDriverWait(driver, 10)
    x = driver.find_element(By.XPATH, var1)
    x.click()
    WebDriverWait(driver, 30)
    driver.find_element(
        By.CSS_SELECTOR, 'a[class*="btn btn-primary btn-block btn-sm"]').click()
    WebDriverWait(driver, 10)
    time.sleep(10)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
    act.send_keys(Keys.ENTER).perform()
    time.sleep(800)
    driver.close()


def twohr(var1):
    os.environ['PATH'] += r"C:/SeleniumDriver"
    driver = webdriver.Chrome()
    act = ActionChains(driver)
    WebDriverWait(driver, 10)
    driver.get("https://myclass.lpu.in/")
    driver.maximize_window()
    driver.find_element(By.NAME, 'i').send_keys(12111097)
    driver.find_element(
        By.CSS_SELECTOR, 'input[type="password"]').send_keys('yourpass')
    WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(driver, 2)
    driver.find_element(
        By.XPATH, '//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()
    WebDriverWait(driver, 10)
    x = driver.find_element(By.XPATH, var1)
    x.click()
    WebDriverWait(driver, 30)
    driver.find_element(
        By.CSS_SELECTOR, 'a[class*="btn btn-primary btn-block btn-sm"]').click()
    WebDriverWait(driver, 10)
    time.sleep(10)
    for i in range(3):
        act.send_keys(Keys.TAB).perform()
    act.send_keys(Keys.ENTER).perform()
    time.sleep(800)
    driver.close()


def timer():
    t = time.localtime()
    this_file = time.strftime("%H:%M:%S", t)
    print("The time is", this_file)


schedule.every(1).seconds.do(timer)


def rest():
    quit()


schedule.every().monday.at("10:03").do(twohr, c1)
schedule.every().monday.at("13:03").do(twohr, c2)
schedule.every().monday.at("16:03").do(onehr, c3)

schedule.every().tuesday.at("09:03").do(onehr, c1)
schedule.every().tuesday.at("11:03").do(twohr, c2)
schedule.every().tuesday.at("14:03").do(onehr, c3)
schedule.every().tuesday.at("15:03").do(onehr, c4)

schedule.every().wednesday.at("09:03").do(onehr, c1)
schedule.every().wednesday.at("11:03").do(twohr, c2)
schedule.every().wednesday.at("14:03").do(onehr, c3)
schedule.every().wednesday.at("15:03").do(onehr, c4)

schedule.every().thursday.at("09:03").do(onehr, c1)
schedule.every().thursday.at("11:03").do(twohr, c2)
schedule.every().thursday.at("14:03").do(onehr, c3)
schedule.every().thursday.at("15:03").do(onehr, c4)

schedule.every().friday.at("10:03").do(onehr, c1)
schedule.every().friday.at("11:03").do(twohr, c2)
schedule.every().friday.at("13:03").do(onehr, c3)

schedule.every().saturday.at("09:03").do(onehr, c1)
schedule.every().saturday.at("10:03").do(onehr, c2)
schedule.every().saturday.at("12:03").do(twohr, c3)
schedule.every().saturday.at("13:03").do(onehr, c4)

schedule.every().saturday.at("16:05").do(rest)

while True:
    schedule.run_pending()
    time.sleep(1)
