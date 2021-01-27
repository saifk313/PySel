from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

name = driver.find_element_by_name("userName")
pwd = driver.find_element_by_name("password")
btnLogin = driver.find_element_by_name("submit")

print("Username field is enabled: ", name.is_enabled())
print("Username field is displayed: ", name.is_displayed())
print("Password field is enabled: ", pwd.is_enabled())
print("Password field is displayed: ", pwd.is_displayed())
print("Submit button is enabled: ", btnLogin.is_enabled())
print("Submit button is displayed: ", btnLogin.is_displayed())

name.send_keys("mercury")
pwd.send_keys("mercury")
btnLogin.click()

time.sleep(3)

linkFlights = driver.find_element_by_link_text("Flights")
linkFlights.click()

time.sleep(3)

roundTrip = driver.find_element_by_xpath("//*[@value='roundtrip']")
oneway = driver.find_element_by_xpath("//*[@value='oneway']")

print("Checkbox round trip is enabled: ", roundTrip.is_enabled())
print("Checkbox round trip is displayed: ", roundTrip.is_displayed())
print("Checkbox one way is enabled: ", oneway.is_enabled())
print("Checkbox one way is displayed: ", oneway.is_displayed())

print("Checkbox round trip is selected:", roundTrip.is_selected())
roundTrip.click()
print("Checkbox round trip is selected:", roundTrip.is_selected())
time.sleep(3)

print("Checkbox one way is selected:", oneway.is_selected())
oneway.click()
print("Checkbox one way is selected:", oneway.is_selected())
time.sleep(2)

driver.quit()