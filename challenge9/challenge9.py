import unittest
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Challenge9(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge9(self):
        #code for our test steps
        API_ENDPOINT = "https://www.copart.com/public/lots/search"
        true = True
        r = requests.post(API_ENDPOINT,data={"query":"ford ranger","freeFormSearch":true},headers={"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
        r_dict=json.loads(r.text)
        output = r_dict['data']['results']['content'][0]
        for i in output:
            textout = str(i)
            textout += str(type(output[i]))
            print(textout)

if __name__ == '__main__':
    unittest.main()