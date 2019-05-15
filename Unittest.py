import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HTMLTestRunner
import HtmlTestRunner
from HTMLTestRunner import HTMLTestRunner
from first.AddToCart import addtocart1
from first.Register import Register

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C://Users/Aram/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Register(self):
        driver = self.driver
        driver.get("http://demo.automationtesting.in")

        reg = Register(driver)
        reg.enter_email("bmnkhan@yahoo.com")
        reg.enter_details1("Aram", "Rokh", "4369 Dufferin ST", "ari1rokh@gmail.com", "6474444223")
        reg.enter_details2("Python", "Canada", "1976", "May", "28")
        reg.enter_password("1234Abc", "1234Abc")
        reg.submit()

        AddtoCart = addtocart1(driver)
        AddtoCart.Practice_site()
        AddtoCart.addtoCart()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner(output="C:/Users/Aram/Downloads/chromedriver_win32/chromedriver.exe"),verbosity = 2)

