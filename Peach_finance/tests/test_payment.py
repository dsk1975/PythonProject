import pytest
from pages.login_page import LoginPage
from pages.payment_page import PaymentPage
from tests.base_test import BaseTest
from config.test_data import TestData as TD
import time

class TestPayment(BaseTest):


    def test_upcoming_payment(self):
        self.login = LoginPage(self.driver)
        self.login.do_login(TD.EMAIL, TD.PASSWORD)
        self.payment = PaymentPage(self.driver)
        title = self.payment.get_payment_page_title(TD.PYAMENT_PAGE_TITLE)
        assert title == TD.PYAMENT_PAGE_TITLE
        button = self.payment.is_clickable(PaymentPage.PAYMENT_BUTTON)
        assert button
        self.payment.click_on_make_payment()
        self.payment.select_upcoming_radiobutton()
        self.payment.click_payment_method()
        self.payment.select_payment_method()
        self.payment.scroll_to_continue_button()
        time.sleep(1)
        cont = self.payment.is_clickable(PaymentPage.CONTINUE_BUTTON)
        assert cont
        self.payment.click_on_continue_button()
        alert = self.payment.get_text(PaymentPage.ALERT_MESSAGE)
        assert alert == TD.PAYMENT_ALERT

