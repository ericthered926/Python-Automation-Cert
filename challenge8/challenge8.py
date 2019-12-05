import unittest
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Challenge8(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge8(self):
        #code for our test steps
        API_ENDPOINT = "https://www.copart.com/public/lots/search"
        true = True
        cars = {"toyota camry": 0, "nissan skyline": 0, "ford ranger": 0, "nissan pathfinder": 0, "audi r8": 0, "tesla model s": 0, "volkswagen golf r": 0, "ford raptor": 0, "subaru sti": 0,"acura nsx": 0}
        for i in cars:
            r = requests.post(API_ENDPOINT,data={"query":i,"freeFormSearch":true},headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
            r_dict=json.loads(r.text)
            cars[i]=r_dict['data']['results']['totalElements']
        print(cars)


if __name__ == '__main__':
    unittest.main()