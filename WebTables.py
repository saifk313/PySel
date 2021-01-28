from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Installers\chromedriver_v88\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

rows = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr"))
cols = len(driver.find_elements_by_xpath("//table[@id='customers']/tbody/tr[1]/th"))

print(rows)
print(cols)

for row in range(2, rows + 1):
    for col in range(1, cols + 1):
        value = driver.find_element_by_xpath("//table[@id='customers']/tbody/tr["+str(row)+"]/td["+str(col)+"]").text
        print(value, end="     ")
    print()
driver.quit()