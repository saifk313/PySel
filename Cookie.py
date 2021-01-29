from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:/Installers/chromedriver_v88/chromedriver.exe")
driver.get("https://www.google.com/")

cookie = driver.get_cookies()
print(len(cookie))
print("Before Addition:", cookie)

cookie = {'name': 'MyCookie', 'value': 'my123'}
driver.add_cookie(cookie)
print(len(cookie))
print("After Addition:", cookie)

driver.delete_cookie('MyCookie')
cookie = driver.get_cookies()
print(len(cookie))
print("After Deletion:", cookie)

driver.delete_all_cookies()
cookie = driver.get_cookies()
print(len(cookie))
print("Delete All:", cookie)

driver.quit()
