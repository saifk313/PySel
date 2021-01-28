from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://demo.guru99.com/test/newtours/")

name = driver.find_element_by_name("userName")
pwd = driver.find_element_by_name("password")
btnLogin = driver.find_element_by_name("submit")

name.send_keys("mercury")
pwd.send_keys("mercury")
btnLogin.click()

time.sleep(3)

linkFlights = driver.find_element_by_link_text("Flights")
linkFlights.click()

wait = WebDriverWait(driver, 10)
roundTrip = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='roundtrip']")))
roundTrip.click()
driver.quit()