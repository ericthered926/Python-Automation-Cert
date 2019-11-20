import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

class Challenge5(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge5(self):
        #code for our test steps
        cars=dict()
        damage=dict()
        def outputList(inputDictionary,inputList):
            for i in inputList:
                model = i.text
                if model in inputDictionary:
                    inputDictionary[model]+=1
                else:
                    inputDictionary[model]=1
            for i in inputDictionary:
                output=i
                output+=' - '
                output+=str(inputDictionary.get(i))
                print(output)
            print("")
            
        self.driver.get("https://www.copart.com")
        searchBox = self.driver.find_element_by_xpath("//header//form[contains(@role,'search')]//input[contains(@type,'text')]")
        searchBox.send_keys('porsche')
        searchBox.send_keys(Keys.ENTER)
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_xpath("//div[contains(@class,'top')]//select/option[contains(@value,'100')]").click()
        self.driver.implicitly_wait(20)
        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//tr[100]/td/span[contains(@data-uname,'lotsearchLotmodel')]")))
        except NoSuchElementException:
            print('No element found')
        carList = self.driver.find_elements_by_xpath("//td/span[contains(@data-uname,'lotsearchLotmodel')]")
        damageList = self.driver.find_elements_by_xpath("//td/span[contains(@data-uname,'lotsearchLotdamagedescription')]")
        outputList(cars,carList)
        outputList(damage,damageList)

if __name__ == '__main__':
    unittest.main()