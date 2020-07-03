from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scripts.bookywayPO import Bookyway
from scripts.bookyway_exception import BookywayException
import argparse
import time
import scripts.util as util
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='Bookyway admin automation\n\nDeveloped by Davide Ponzini')
    parser.add_argument('username', help='file containing a list of usernames')
    parser.add_argument('credits', type=int, help='number of credits to assign to each user')
    parser.add_argument('reason', help='reason to display next to transaction')
    parser.add_argument('--headless', help='use headless browser', action='store_true')

    args, unknown = parser.parse_known_args()
    return args


def init(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    return webdriver.Chrome('./chromedriver.exe', chrome_options=chrome_options)


def set_user_credits(bookyway, username, credits, reason):
    for user in bookyway.query(username).get_users():
        util.log(user)

        credits_page = user.get_credits()
        if credits_page is None:
            util.warn('User has unlimited credits')
            continue

        credits_page.set(credits, reason)


if __name__ == '__main__':
    args = parse_args()
    browser = init(headless=args.headless)

    util.log('{}\nQuery={}\nCredits={}\nReason={}'.format(
        datetime.now(),
        args.username,
        args.credits,
        args.reason
    ))

    try:
        bookyway = Bookyway(browser)

        set_user_credits(bookyway, args.username, args.credits, args.reason)
    except BookywayException as e:
        print('[!!!] {}'.format(e.message))
    finally:
        time.sleep(2)
        browser.quit()
