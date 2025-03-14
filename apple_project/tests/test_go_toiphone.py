from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone
from playwright.sync_api import Page
import time


def test_gotoiphone(page: Page):
    apple_web = AppleWebsite(page)
    apple_web.navigate()
    apple_web.clickonwebsite()
    apple_iphone = GotoIphone(page)
    apple_iphone.clickoniphone()
    time.sleep(4)
    
