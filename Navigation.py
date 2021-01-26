from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")
driver.get("https://www.youtube.com/")
time.sleep(4)
driver.get("https://www.google.com/")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver,quit()