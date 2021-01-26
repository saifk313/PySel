from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browserName = "chrome"

if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == 'firefox':
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("Please enter a valid browser name: " + browserName)
#raise exception

driver.get("http://demo.guru99.com/test/newtours/register.php")
firstname = driver.find_element(By.NAME, "firstName").send_keys("SAIF")
lastname = driver.find_element(By.ID, "password").send_keys("SAIF")
login_button = driver.find_element(By.ID, "loginBtn").click()

time.sleep(3)
driver.quit()