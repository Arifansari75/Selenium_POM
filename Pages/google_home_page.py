import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class GoogleHomePage():
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com/"

    def click_on_google_apps_buton(self):
        """This method is used to click on Google Home page"""
        self.driver.find_element(By.XPATH, "//a[@class='gb_B' and @aria-label='Google apps']").click()
        time.sleep(1)

    def load_url(self):
        self.driver.get(self.url)

    def list_of_all_google_apps(self):
        """This method is used to get list all Google apps"""
        self.click_on_google_apps_buton()
        self.driver.switch_to.frame("app")
        l = self.driver.find_elements(By.XPATH, "//div[@class='o83JEf' and @jsname='sLJ6md']/div/ul/li/a")
        time.sleep(1)
        l1 = []
        for i in l:
            l1.append(i.text)
        self.driver.switch_to.default_content()
        return l1

    def google_search_with_text(self, search_text):
        """This method will send provide text in search bar and hit enter"""
        self.driver.find_element(By.XPATH,"//textarea[@name='q']").send_keys(search_text)
        self.driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']/center/input[1]").click()
        time.sleep(2)

    def list_of_all_languages(self):
        """This method is used to get list all languages Google offered in"""
        list_of_languages = self.driver.find_elements(By.XPATH,"//div[@id='SIvCob']/a")
        l = []
        for i in list_of_languages:
            l.append(i.text)
        return l







