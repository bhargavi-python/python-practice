from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone
from lib.apple_addfeatures import AddFeatures
from lib.apple_addtothebag import AddtoBag
from playwright.sync_api import Page


def test_addtobag(page: Page):
    apple = AppleWebsite(page)
    apple.navigate()
    apple.clickonwebsite()
    iphone = GotoIphone(page)
    iphone.clickoniphone()
    features = AddFeatures(page)
    features.clickonfeatures()
    bag = AddtoBag(page)
    bag.clickaddtobag()

