from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\\Installers\\chromedriver_v88\\chromedriver.exe")

driver.get("https://www.nopcommerce.com/en")
print(driver.current_url)
print(driver.current_window_handle)
title = driver.title
print(title)
driver.close()