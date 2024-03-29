import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Challenge2(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge2(self):
        #code for our test steps
        self.driver.get("https://www.copart.com")
        searchBox = self.driver.find_element_by_xpath("//header//form[contains(@role,'search')]//input[contains(@type,'text')]")
        searchBox.send_keys('exotics')
        searchBox.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'checkbox')]/label/abbr[contains(@value,'Porsche')]")))
        assert self.driver.find_element_by_xpath("//div[contains(@class,'checkbox')]/label/abbr[contains(@value,'Porsche')]")

if __name__ == '__main__':
    unittest.main()