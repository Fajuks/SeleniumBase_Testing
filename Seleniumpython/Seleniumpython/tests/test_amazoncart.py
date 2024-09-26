from seleniumbase import BaseCase

class AmazonCartTestCase(BaseCase):
    def test_amazon_cart(self):
        #load the home page
        self.open("https://www.amazon.ca")
        self.sleep(10)

        # # search for a product
        # if self.is_element_visible("#twotabsearchtextbox"):
        #     print("Element is Visible")
        #     self.sleep(4)
        #     self.send_keys("#twotabsearchtextbox", "ps5")
        #     self.sleep(5)
        #
        # #clik the search button
        # self.click("#nav-search-submit-button")
        # self.sleep(5)
        #
        # #select any searched item and add to the cart
        # self.click('[alt="PlayStation 5 Console - Disc Edition [Model 3005720]"]')
        # self.sleep(5)
        # self.click("#add-to-cart-button-ubb")
        # self.sleep(3)

        # search for a product 2
        if self.is_element_visible("#twotabsearchtextbox"):
            print("Element is Visible")
            self.sleep(3)
            self.send_keys("#twotabsearchtextbox", "xbox")
            self.sleep(6)

        # clik the search button
        self.click("#nav-search-submit-button")
        self.sleep(5)

        # select any searched item and add to the cart 2
        self.click('[alt = "Xbox Series X Console"]')
        self.sleep(5)
        self.click("#add-to-cart-button")
        self.sleep(3)
        self.click("#attachSiNoCoverage-announce")
        self.sleep(2)
        # confirm if the item is added to the cart
        if self.assert_text("1","#nav-cart-count"):
            print("The correct number of element is in the cart")
        else:
            print("The correct number of element is not in the cart")

        #go to the cart
        #self.click('data-csa-c-content-id="sw-gtc_CONTENT"]')
        self.click("#sw-gtc")
        self.sleep(5)
        #increase the item and confirm the price changes
        self.click(".a-button-text.a-declarative" )
        self.sleep(5)
        self.click('[aria-labelledby="quantity_2"]')
        self.sleep(2)

        self.assert_text("$1,299.92","#sc-subtotal-amount-activecart")
        # get_text = self.get("#sc-subtotal-amount-activecart")
        # self.assert_true(get_text, "$1,299.92") WE can also try those methods

        #self.wait_for_element_visible("")#this helps when we are dealing(waiting for) with loading screen
        #self.wait_for_element_not_visible("")#this is called after the load screen disappear