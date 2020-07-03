from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import scripts.conf as conf
import time
from scripts.bookyway_user_creditsPO import BookywayUserCredits


class BookywayUser:
    def __init__(self, browser: webdriver.Chrome, element: WebElement):
        self.browser = browser
        self.element = element

        self.name = self.element.find_element_by_css_selector(conf.SELECTOR_ACCOUNTS_USERS_NAME).text

    def __str__(self):
        return self.name

    def edit(self):
        self.element.find_element_by_css_selector(conf.SELECTOR_ACCOUNTS_USERS_EDIT).click()
        time.sleep(conf.SLEEP_QUERY)

        return self

    def get_credits(self):
        self.edit()

        credits = self.browser.find_element_by_css_selector(conf.SELECTOR_ACCOUNTS_USERS_CREDITS)
        if credits.value_of_css_property('display') == 'none':
            return None

        credits.click()
        time.sleep(conf.SLEEP_QUERY)

        form = self.browser.find_element_by_css_selector(conf.SELECTOR_CREDITS)

        return BookywayUserCredits(self.browser, form, self)
