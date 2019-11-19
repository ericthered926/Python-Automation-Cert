import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge3(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge3(self):
        #code for our test steps
        self.driver.get("https://www.copart.com")
        popularSearch = self.driver.find_elements_by_xpath("//div[contains(@ng-if,'popularSearches')]//li/a")
        for popular in popularSearch:
            s=popular.text
            s+=" - "
            s+=popular.get_attribute("href")
            print(s)

if __name__ == '__main__':
    unittest.main()