import time

import slash
from selenium import webdriver

from ..Pages.google_home_page import GoogleHomePage
# from ..slashconf import Driver


class GoogleHomeTest(slash.Test):
    @slash.use_fixtures(["Driver"])
    def before(self,Driver):
        print("Inside before")
        self.googleHomePage = GoogleHomePage(Driver)
        print("outside before")

    def test_test1(self):
        self.googleHomePage.load_url()
        list_of_google_apps = self.googleHomePage.list_of_all_google_apps()
        print(len(list_of_google_apps))
        print("Inside test1",list_of_google_apps)
        # self.googleHomePage.google_search_with_text("Python W3 school")
        list_of_language = self.googleHomePage.list_of_all_languages()
        print(len(list_of_language),list_of_language)