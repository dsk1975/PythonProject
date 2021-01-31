from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    username_field = (By.NAME,'login_email')
    password_field = (By.NAME, 'login_password')
    sing_in_button = (By.XPATH, "//div[@class='signin-text']")
    account_nemu = (By.XPATH, "//span[contains(text), 'HA']")
    def login(self, username, password):
        self.send_keys(self.username_field, username)
        self.send_keys(self.password_field, password)
        self.click(self.sing_in_button)

        self.is_visible(self.account_nemu)

