from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import scripts.conf as conf
import time


class BookywayUserCredits:
    def __init__(self, browser: webdriver.Chrome, form: WebElement, parent):
        self.browser = browser
        self.form = form
        self.parent = parent

        self.credits = int(self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_CURRENTCREDITS).text)

        self.add_button = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_ADD)
        self.remove_button = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_REMOVE)
        self.amount = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_NEWCREDITS)
        self.note = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_NOTE)
        self.save_button = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_SAVE)
        self.cancel_button = self.form.find_element_by_css_selector(conf.SELECTOR_CREDITS_CANCEL)

    def __str__(self):
        return self.credits

    def get(self):
        self.close()
        return self.credits

    def add(self, amount: int, note='Added credits'):
        self.add_button.click()

        self.amount.clear()
        self.amount.send_keys(amount)

        self.note.send_keys(conf.NOTE_MESSAGE.format(note))

        self.save_button.click()
        time.sleep(conf.SLEEP_CREDITSAVE)

        return self.parent

    def remove(self, amount: int, note='Removed credits'):
        self.remove_button.click()

        self.amount.clear()
        self.amount.send_keys(amount)

        self.note.send_keys(conf.NOTE_MESSAGE.format(note))

        self.save_button.click()
        time.sleep(conf.SLEEP_CREDITSAVE)

        return self.parent

    def set(self, amount: int, note='Set credits'):
        if self.credits < amount:
            return self.add(amount - self.credits, note)
        elif self.credits > amount:
            return self.remove(self.credits - amount, note)

    def close(self):
        self.cancel_button.click()
