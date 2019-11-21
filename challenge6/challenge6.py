import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Challenge6(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge6(self):
        #code for our test steps
        self.driver.get("https://www.copart.com")
        searchBox = self.driver.find_element_by_xpath("//header//form[contains(@role,'search')]//input[contains(@type,'text')]")
        searchBox.send_keys('nissan')
        searchBox.send_keys(Keys.ENTER)
        wait = WebDriverWait(self.driver, 10)
        assert wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Model')]")))
        self.driver.find_element_by_xpath("//a[contains(.,'Model')]").click()
        try:
            assert wait.until(EC.element_to_be_clickable((By.XPATH, "//h4[contains(.,'Model')]/..//ul/li//abbr[contains(.,'kyline')]")))
            self.driver.find_element_by_xpath("//h4[contains(.,'Model')]/..//ul/li//abbr[contains(.,'kyline')]").click()
        except:
            self.driver.save_screenshot("screenshot.png")


if __name__ == '__main__':
    unittest.main()