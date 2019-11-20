import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Challenge4(unittest.TestCase):

    def setUp(self):
        #code to startup webdriver
        self.driver = webdriver.Chrome("../env/chromedriver")

    def tearDown(self):
        #code to close webdriver
        self.driver.close()

    def test_challenge4(self):
        #code for our test steps
        def fibonacciCalc(n):
            if n <= 1:
                return n
            else:
                return(fibonacciCalc(n-1) + fibonacciCalc(n-2))
        x = list()
        num2words = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 5: 'five', 8: 'eight', 13: 'thirteen', 21: 'twenty one'}
        for i in range(9):
            x.append(fibonacciCalc(i))
        for i in range(len(num2words)):
            output=str(x[i])
            output+=' - '
            output+=num2words[x[i]]
            print(output)

if __name__ == '__main__':
    unittest.main()