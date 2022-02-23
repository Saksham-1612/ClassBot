import os
import time
# import schedule

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] += r"C:/SeleniumDriver"
driver = webdriver.Chrome()
act = ActionChains(driver)
WebDriverWait(driver, 10)
driver.get("https://myclass.lpu.in/")
driver.maximize_window()
user = driver.find_element(By.NAME, 'i').send_keys(12111097)
driver.find_element(By.CSS_SELECTOR, 'input[type="password"]').send_keys('Your Password')
WebDriverWait(driver, 10)
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
WebDriverWait(driver, 2)
driver.find_element(By.XPATH, '//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()
WebDriverWait(driver, 10)
x = driver.find_element(By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div'
                                  '/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]')
x.click()
WebDriverWait(driver, 30)
driver.find_element(By.CSS_SELECTOR, 'a[class*="btn btn-primary btn-block btn-sm"]').click()
WebDriverWait(driver, 10)
time.sleep(10)
for i in range(3):
    act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.ENTER).perform()
# driver.close()
