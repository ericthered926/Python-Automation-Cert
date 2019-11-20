import unittest
from selenium import webdriver

class Challenge6(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge6(self):
        #code for our test steps
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

if __name__ == '__main__':
    unittest.main()