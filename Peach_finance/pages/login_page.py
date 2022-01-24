from config.test_data import TestData as TD
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.basepage import BasePage

class LoginPage(BasePage):

    PAGE_TITLE = (By.XPATH, '/span[@data-testid="logo"]')
    INPUT_EMAIL = (By.NAME, 'email')
    INPUT_PASSWORD = (By.NAME, 'password')
    CONTINUE_BUTTON = (By.XPATH, '//button[@data-cy="submit"]')
    LOGIN_URL = TD.LOGIN_URL

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TD.LOGIN_URL)

    def do_login(self,username, password):
        """
        input login/password and push button Submit on the Login Page
        :param login:
        :param password:
        :return:
        """
        self.do_send_keys(LoginPage.INPUT_EMAIL,username)
        self.do_send_keys(LoginPage.INPUT_PASSWORD,password)
        self.click(LoginPage.CONTINUE_BUTTON)

