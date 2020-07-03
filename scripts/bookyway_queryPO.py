from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import scripts.conf as conf
import time
from scripts.bookyway_userPO import BookywayUser


class BookywayQuery:
    def __init__(self, browser: webdriver.Chrome, query=None):
        self.browser = browser

        self.browser.get(conf.ACCOUNTS_PAGE)

        field_query = self.browser.find_element_by_css_selector(conf.SELECTOR_ACCOUNTS_QUERYTEXT)
        button_query_confirm = self.browser.find_element_by_css_selector(conf.SELECTOR_ACCOUNTS_QUERYSUBMIT)

        if query is not None:
            field_query.send_keys(query)
            button_query_confirm.click()
            time.sleep(conf.SLEEP_QUERY)

    def get_users(self):
        # `while` loop takes care of pagination
        while True:
            users = self.browser.find_elements_by_css_selector(conf.SELECTOR_ACCOUNTS_USERS)

            for user in users:
                yield BookywayUser(self.browser, user)

            try:
                self.browser.find_element_by_id(conf.SELECTOR_ACCOUNTS_NEXTPAGE).click()
                time.sleep(conf.SLEEP_QUERY)
            except NoSuchElementException:
                break
