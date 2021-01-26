from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Installers\\chromedriver_v88\\chromedriver.exe")
driver.implicitly_wait(3)
driver.get("http://www.google.com")
driver.find_element(By.NAME, "q").send_keys('naveen automation')
list_results = driver.find_elements(By.CSS_SELECTOR, 'ul.erkvQe li span')
time.sleep(3)
print(len(list_results))

for result in list_results:
    print(result.text)
    if result.text == 'naveen automation labs':
        result.click()
        break

time.sleep(2)
driver.quit()