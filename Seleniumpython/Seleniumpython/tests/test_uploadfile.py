from nose import selector
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
import  time
class UploadFileTestCase(BaseCase):
    def test_upload_file(self):
        #open the page
        self.open("https://the-internet.herokuapp.com/upload")

        #get the file path
        file_path ="/Users/fajukoodunayo/Downloads/AfricaMap.jpg"

        #upload file
        self.choose_file("#file-upload", file_path, by="css selector")
        #time.sleep(10)

        # click the upload button
        self.click("#file-submit")

        #assert the upload text
        upload_text= self.get_text( " .example h3")
        self.assert_equal(upload_text, "File Uploaded!")
        #self.assert_text("File Uploaded!", "h3")


    def test_upload_second(self):
        self.open("https://www.filemail.com/share/upload-file")

        # input the title
        if self.is_element_visible("#FilemailSubjectURL", by="css selector"):
            print("element visible")
            self.send_keys("#FilemailSubjectURL","Just a test phase", by="css selector")
            time.sleep(3)
        else:
            print("element not visible")

        #input a short message
        if self.is_element_visible("#FilemailMessageToURL", by="css selector"):
            print("element visible")
            self.send_keys("#FilemailMessageToURL","You can reach me if you want for more testing!!!", by="css selector")
            time.sleep(3)
        else:
            print("element not visible")

        #upload a file or a folder(first you get the file path)

        #get the file path
        file_path2= "/Users/fajukoodunayo/Downloads/AfricaMap.jpg"

        #upload the file
        #self.choose_file(".fup-picker-label input[type='file']", file_path2, by="css selector")
        #input[type='file'] : s a general selector that helps to capture any <input> element in HTML that is specifically designed for handling file uploads.
        self.choose_file(".fup-picker-label input[type='file']", file_path2, by="css selector")#we are making it specific
        time.sleep(3)
        # click the submit button
        self.click("#sendBtn")

        #check for the confirmation message