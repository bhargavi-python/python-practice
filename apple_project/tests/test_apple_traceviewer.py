from playwright.sync_api import sync_playwright, Page
from lib.search import AppleWebsite
from lib.apple_gotoiphone import GotoIphone
from lib.apple_addfeatures import AddFeatures
from lib.apple_addtothebag import AddtoBag


def test_traceviewer(page: Page):
    with sync_playwright() as p:
        # browser = p.chromium.launch(headless=False)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.tracing.start(
            screenshots=True, snapshots=True, sources=True)
        page = context.new_page()
        # page.goto("https://www.google.com")
        search = AppleWebsite(page)
        search.navigate()
        search.clickonwebsite()
        iphone = GotoIphone(page)
        iphone.clickoniphone()
        features = AddFeatures(page)
        features.clickonfeatures()
        cart = AddtoBag()
        cart.clickaddtobag()
        context.tracing.stop(path="trace.zip")
        context.close()
