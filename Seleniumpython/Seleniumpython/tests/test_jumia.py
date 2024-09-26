import time

from seleniumbase import BaseCase

class JumiaTestCase(BaseCase):
    def test_jumia(self):
        self.open('https://www.jumia.com.ng/') # this command helps to open the jumia site.
        self.sleep(5)  #bafter opening the site, the program waits for 5 seconds before carrying any other operation

        for i in range(1,13):# a loop to iterate through all the menu bars
            index_num=f'/main/div[1]/div[1]/div[1]/div/a[{i}]'
            selector=f'//*[@id="jm"]{index_num}'
            self.sleep(5)

            if index_num == '/main/div[1]/div[1]/div[1]/div/a[3]':
                self.click('#jm > main > div.row.-pv`m > div.col16.-df.-j-bet.-pbs > div.flyout-w.-fsh0.-fs0 > div > a:nth-child(5)')
                self.sleep(2)
                print("element was clicked ")

            self.click('[aria-label="Jumia Nigeria: Online Shopping for Electronics, Phones & Fashion"]')
            self.sleep(3)

            get_text = self.get_text(selector)
            self.sleep(2)
            if self.is_element_visible(selector):
                print("element is visible")
                self.sleep(2)
                print(f"after checking the index{index_num} we saw the text{get_text}")

            else:
                print(f"element with the id {index_num} is not visible")

