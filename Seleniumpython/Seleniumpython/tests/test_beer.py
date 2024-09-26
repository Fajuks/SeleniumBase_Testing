from seleniumbase import BaseCase
from seleniumbase.common.exceptions import NoSuchElementException

class BeerTestCase(BaseCase):
    def test_beer(self):
        #open the beer store
        self.open("https://www.thebeerstore.ca/")
        self.sleep(3)

        #search for an item
        if self.is_element_visible('[placeholder="Search our best value and brands"]'):
            print("element is visible")
            self.send_keys('[placeholder="Search our best value and brands"]', "beer")
            self.sleep(2)
        else:
            print("element is not visible")
        #click the search button
        self.click('[aria-label="Search"]')
        self.sleep(3)

        try:
            self.assert_element('[alt="LECH BEER"]')
        except NoSuchElementException:
            if self.is_text_visible("No result found!",".text-center.mb-0px"):
                print("Text is visible")
            else:
                print("Text is not visible")


