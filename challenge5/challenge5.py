import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge5(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge5(self):
        #code for our test steps

if __name__ == '__main__':
    unittest.main()