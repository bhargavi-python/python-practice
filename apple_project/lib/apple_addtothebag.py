from playwright.sync_api import Page
import time


class AddBag:

    loc_1 = "//label[@id='noTradeIn_label']"
    loc_2 = "(//label[@id='applecareplus_58_noapplecare_label'])[1]"
    loc_3 = "//button[@title='Add to Bag']"
    loc_4 = "//button[normalize-space()='Review Bag']"


class AddtoBag:

    def __init__(self, page: Page):
        self.page = page

    def clickaddtobag(self):
        self.page.locator(AddBag.loc_1).click()
        self.page.locator(AddBag.loc_2).click()
        self.page.locator(AddBag.loc_3).click()
        self.page.locator(AddBag.loc_4).click()
        time.sleep(4)
