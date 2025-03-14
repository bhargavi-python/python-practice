from playwright.sync_api import Page
import time


class IphoneFeatures:
    label = "span.form-label-small"
    label_1 = "img.colornav-swatch"
    label_2 = "(//span[@class='column form-selector-left-col rf-bfe-selector-left-col'])[5]"


class AddFeatures():

    def __init__(self, page: Page):
        self.page = page

    def clickonfeatures(self):
        self.page.locator(IphoneFeatures.label).nth(0).click()
        self.page.locator(IphoneFeatures.label_1).nth(0).click()
        self.page.wait_for_timeout(3000)
        # self.page.locator(IphoneFeatures.label_2).all()
        self.page.locator(IphoneFeatures.label_2).click()
        time.sleep(4)
        

