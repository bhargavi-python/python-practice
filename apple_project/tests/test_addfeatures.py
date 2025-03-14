from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone
from lib.apple_addfeatures import AddFeatures
from playwright.sync_api import Page
import time


def test_addfeatures(page: Page):
    apple = AppleWebsite(page)
    apple.navigate()
    # apple.clickonwebsite()
    # iphone = GotoIphone(page)
    # iphone.clickoniphone()
    # features = AddFeatures(page)
    # features.clickonfeatures()
    # time.sleep(4)


