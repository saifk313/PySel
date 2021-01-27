from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/reservation.php")

drp = Select(driver.find_element_by_name("fromPort"))
print(len(drp.options))

for option in drp.options:
    print(option.text)

drp.select_by_index(2)
time.sleep(1)
drp.select_by_value("Frankfurt")
time.sleep(1)
drp.select_by_visible_text("Acapulco")
time.sleep(1)

driver.quit()