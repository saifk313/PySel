from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")

driver.get("https://www.google.com/")

driver.save_screenshot("D:/google.png")
time.sleep(1)

driver.get_screenshot_as_file("D:/google.jpg") # Will issue warnings

driver.quit()