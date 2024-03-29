import unittest
from selenium import webdriver


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        print('Initialize test environment')
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            print('Cleanup test enviroment')
            self.driver.close()
            self.driver.quite()