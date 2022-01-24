
from pages.basepage import BasePage
from selenium.webdriver.common.by import By

class PaymentPage(BasePage):

    PAYMENT_BUTTON = By.XPATH, '//*[text() = "Make a payment"]'
    UPCOMING_OVERDUE = By.XPATH, '//label[@data-testid = "label-no-custom-field"][@for= "Upcoming + Overdue"]'
    CLICK_METHOD = By.CSS_SELECTOR, '.select__indicators'
    SELECT_METHOD = By.CSS_SELECTOR, 'div[id^="react-select-"]'
    CONTINUE_BUTTON = By.XPATH, '//button[@data-cy="submit"]'
    ALERT_MESSAGE = By.CSS_SELECTOR, '.message-status .message'

    def __init__(self, driver):
        super().__init__(driver)

    def get_payment_page_title(self, title):
        return self.get_title(title)

    def click_on_make_payment(self):
        self.click(PaymentPage.PAYMENT_BUTTON)

    def select_upcoming_radiobutton(self):
        self.click(PaymentPage.UPCOMING_OVERDUE)

    def click_payment_method(self):
        self.click(PaymentPage.CLICK_METHOD)

    def select_payment_method(self):
        self.click(PaymentPage.SELECT_METHOD)

    def click_on_continue_button(self):
        self.click(PaymentPage.CONTINUE_BUTTON)

    def scroll_to_continue_button(self):
        self.scroll_to_bottom(PaymentPage.CONTINUE_BUTTON)