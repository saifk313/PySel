from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")

driver.implicitly_wait(10)

driver.get("http://demo.guru99.com/test/newtours/")

driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()

driver.quit()