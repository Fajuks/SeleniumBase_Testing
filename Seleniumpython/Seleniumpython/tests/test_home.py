#from tkinter.constants import SEL_FIRST

from seleniumbase import BaseCase

class HomeTest(BaseCase): #we are passing thr Base as an argument so that we cah have access to the Basecase iin out Hometest class.
    #simple word inheritance, so our Hometest class can have access to all the library the Basecase will provide
    def test_home_page(self):#this iue class method definition The self represent the instance of the class, by using the self we can access the attribute as well as the method if the class in python
        self.open("https://www.instagram.com/")

        # self.assert_text("WordPress website creation made easy.", "[role='heading'] .dc-theme-white",by="css selector")
        # self.click(".mdc-button__label.reg-mdc-button__label.mdc-theme-primary--dark", by="css selector")
        #get_test_url=self.get_current_url() #we are trying to get the current url after clicking the botton.
        # self.assert_equal(get_test_url,"https://www.bluehost.com/hosting/shared#pricing-cards")#we are checking if the current url matches the url passed as an argument
        # assert is used to verify a certain condition

        # self.scroll_to(".p__small.dc-theme-white",by="css selector")
        # self.assert_text("© 2002-", ".p__small.dc-theme-white",by="css selector")
        self.scroll_to_bottom()
        self.assert_text("© 2024 Instagram from Meta", ".x1d52u69.x1n2onr6",by="css selector")
        # self.scroll_to(".x1lliihq.x1plvlek.xryxfnj", by="css selector")


    def test_menu_links(self):
        #open url
        self.open("https://www.amazon.ca/")
        self.sleep(10)

        #find menu links element now we are using xpath
        # whatisthis=self.find_element('[data-csa-c-slot-id="nav_cs_0"]', by="css selector")
        # print(whatisthis.text)

        # Find and interact with the element using the CSS selector directly
        #element = self.find_element('[data-csa-c-slot-id="nav_cs_0"]', by="css selector")
        # for i in range(0, 4):  # Loop through numbers 1 to 3
        #     slot_id = f'nav_cs_{i}'  # Construct the data-csa-c-slot-id value
        #     selector = f'[data-csa-c-slot-id="{slot_id}"]'  # Create the CSS selector
        #
        #     # Check if the element exists
        #     if self.is_element_visible(selector, by="css selector"):
        #         # Fetch the text content of the element
        #         element_text = self.get_text(selector, by="css selector")
        #
        #         # Print the text
        #         print(f"Element with data-csa-c-slot-id={slot_id} has text: {element_text}")
        #
        #         # Interact with the element (e.g., click it)
        #         self.click(selector, by="css selector")
        #     else:
        #         print(f"Element with data-csa-c-slot-id={slot_id} not found")

        #expected_nav=["Best Sellers", "Audible", "Deals Store", "New Releases"]
        for i in range(0,4):
            num_id =f'nav_cs_{i}'
            selector =f'[data-csa-c-slot-id="{num_id}"]'

            if self.is_element_visible(selector, by="css selector"):
                element_text= self.get_text(selector, by="css selector")

                self.click(selector, by="css selector")

                if num_id == 'nav_cs_0':
                    self.click('[data-csa-c-slot-id="nav_cs_0"]', by="css selector")
                    self.scroll_to(".navFooterBackToTop", by="css selector")
                    self.sleep(3)
                    self.click(".navFooterBackToTop", by="css selector")
                    self.sleep(3)
                    print("Scrolled to the bottom and clicked 'Back to Top'")


                #self.assert_equal(element_text, expected_nav[i])
                print(f'after checking the nav with the id: {num_id} we found the text:{element_text}')

            else:
                print(f'we could not find the element with the nav{num_id}')