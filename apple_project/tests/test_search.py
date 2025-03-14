import time
from lib.search import AppleWebsite
from playwright.sync_api import Page


def test_searchapple(page: Page):
    apple = AppleWebsite(page)
    # time.sleep(3)
    apple.navigate()
    apple.clickonwebsite()
    time.sleep(3)


