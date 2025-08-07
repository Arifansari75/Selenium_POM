from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print("dd",driver)
driver.get("https://google.com")
list_of_languages = driver.find_elements(By.XPATH,"//div[@id='SIvCob']/a")
l = []
for i in list_of_languages:
    l.append(i.text)
print(l)