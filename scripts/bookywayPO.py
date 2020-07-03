from selenium import webdriver
import time
import scripts.conf as conf
import secret
import scripts.util as util
from scripts.bookyway_queryPO import BookywayQuery

class Bookyway:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

        self.login()

    def login(self):
        self.browser.get(conf.LOGIN_PAGE)
        field_username = self.browser.find_element_by_css_selector(conf.SELECTOR_LOGIN_USERNAME)
        field_password = self.browser.find_element_by_css_selector(conf.SELECTOR_LOGIN_PASSWORD)
        button_confirm = self.browser.find_element_by_css_selector(conf.SELECTOR_LOGIN_CONFIRM)

        field_username.send_keys(secret.USERNAME)
        field_password.send_keys(secret.PASSWORD)
        button_confirm.click()

        time.sleep(conf.SLEEP_LOGIN)
        if self.browser.current_url == conf.LOGIN_PAGE:
            util.error_quit('Login unsuccessful')
        else:
            util.log('Login successful')

    def query(self, query_text):
        return BookywayQuery(self.browser, query_text)
