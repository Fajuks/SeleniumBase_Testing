from seleniumbase import BaseCase
from package_obj.home_page import Homepage

class TestNew(BaseCase):

    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        self.open("https://www.hostinger.com/")

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_new(self):

        # self.click("#hgr-topmenu-login", by="css selector")
        # self.click('[data-click-id="hgr-header-cta-get_started"]', by="css selector")

        if self.is_element_visible(Homepage.loginselector, by="css selector"): # for this i imported the selector which has been assigned to a variable in the Homepage
            print(f"Element is visible")
            self.click("#hgr-topmenu-login", by="css selector")
        else:
            print(f"Element is not visible")

    def test_started(self):
        if self.is_element_visible('[data-click-id="hgr-header-cta-get_started"]', by="css selector"):
            print(f"Element is visible")
            self.click('[data-click-id="hgr-header-cta-get_started"]', by="css selector")
        else:
            print(f"Element is not visible")