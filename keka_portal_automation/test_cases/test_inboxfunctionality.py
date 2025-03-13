
from data import config
from lib.login import Loginpage
from lib.inboxfunction import InboxFunctionality


class TestInboxFunction():

    url = config.base_url
    user = config.username
    password = config.password

    def test_Inboxfunctionality(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.log = Loginpage(self.driver)
        self.log.clickonpassword()
        self.log.set_username(self.user)
        self.log.set_password(self.password)
        self.log.clickonlogin()

        self.inbox = InboxFunctionality(self.driver)
        self.inbox.checkonInbox()
