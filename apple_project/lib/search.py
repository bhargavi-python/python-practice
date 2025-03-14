from playwright.sync_api import Page


class SearchPage:
    search_loc = "//input[@title='Search']"
    locate_apple = "//h3[normalize-space()='Apple (India)']"


class AppleWebsite:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.google.com")

    def clickonwebsite(self):
        self.page.wait_for_timeout(4000)
        self.page.locator(SearchPage.search_loc).click()
        self.page.locator(SearchPage.search_loc).fill("Apple")
        self.page.locator(SearchPage.search_loc).press("Enter")
        self.page.locator(SearchPage.locate_apple).click()
(4000)