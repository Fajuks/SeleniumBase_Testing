from time import sleep

from nose import selector
import time
from seleniumbase import BaseCase
from seleniumbase.fixtures.js_utils import convert_to_css_selector


class InputTest(BaseCase):

    def test_input_text(self):
        # self.open("https://ashleighrichards.com/contact")
        # self.assert_text( "We Would Like To Hear From You",  "[data-aid='CONTACT_FORM_TITLE_REND']", by="css selector" )
        # expected_text= self.get_text('[data-aid="CONTACT_FORM_TITLE_REND"]', by="css selector")
        # print(f"the expected tex is {expected_text}")


        # Open the page
        self.open("https://ashleighrichards.com/contact")

        # fill up the forms

        if self.is_element_visible('[data-aid="CONTACT_FORM_NAME"] .c2-2v', by="css selector"):
            print("element visible")
            self.send_keys('[data-aid="CONTACT_FORM_NAME"] .c2-2v', "James Bond", by="css selector")
            time.sleep(1)
        else:
            print("element not visible")
        if self.is_element_visible('[data-aid="CONTACT_FORM_EMAIL"] .c2-2v', by = "css selector"):
            print("element visible")
            self.send_keys('[data-aid="CONTACT_FORM_EMAIL"] .c2-2v', "Reple1981@cuvox.de", by = "css selector")
            time.sleep(1)
        else:
            print("element not visible")
        if self.is_element_visible('[data-aid="CONTACT_FORM_PHONE"] .c2-2v', by = "css selector"):
            print("element visible")
            self.send_keys('[data-aid="CONTACT_FORM_PHONE"] .c2-2v', "2245839593")
            time.sleep(1)
        else:
            print("element not visible")
        if self.is_element_visible( '[data-aid="Tell us about your project and timeline."]', by = "css selector"):
            print("element visible")
            self.send_keys('[data-aid="Tell us about your project and timeline."]', "I am just a tester")
            time.sleep(1)
        else:
            print("element not visible")

        self.click('[data-aid="CONTACT_SUBMIT_BUTTON_REND"]', by="css selector")
        time.sleep(5)

        #self.assert_text("Thank you for your inquiry! We will get back to you within 48 hours.", '[data-aid="CONTACT_FORM_SUBMIT_SUCCESS_MESSAGE"]' )
        message_text = self.get_text('[data-aid="CONTACT_FORM_SUBMIT_SUCCESS_MESSAGE"]')
        self.assert_equal(message_text, "Thank you for your inquiry! We will get back to you within 48 hours.")

