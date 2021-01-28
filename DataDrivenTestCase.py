import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.implicitly_wait(15)

path = "C:/Users/Dell/Desktop/serene.xlsx"
rows = XLUtils.get_row_count(path, 'Sheet1')
# cols = XLUtils.get_column_count(path, 'Sheet1')

for row in range(2, rows + 1):
    username = XLUtils.read_data(path, 'Sheet1', row, 1)
    password = XLUtils.read_data(path, 'Sheet1', row, 2)

    driver.find_element_by_name("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("submit").click()

    if driver.title == "Login: Mercury Tours":
        print("Test Case Passed")
        XLUtils.write_data(path, 'Sheet1', row, 3, "Passed")
    else:
        print("Test Case Failed")
        XLUtils.write_data(path, 'Sheet1', row, 3, "Failed")

    driver.find_element_by_link_text("Home").click()
driver.quit()