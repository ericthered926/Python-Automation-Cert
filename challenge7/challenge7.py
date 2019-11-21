import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Challenge7(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge7(self):
        #code for our test steps
        self.driver.get("https://www.copart.com")
        arr = []
        popularSearch = self.driver.find_elements_by_xpath("//div[contains(@ng-if,'popularSearches')]//a")
        for popular in popularSearch:
            s=popular.text
            h=popular.get_attribute("href")
            ar = [s,h]
            arr.append(ar)
        print(arr)


if __name__ == '__main__':
    unittest.main()