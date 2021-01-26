from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.current_url)
print(driver.title)
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(4)
driver.close() # closes the window currently in focus
driver.quit()