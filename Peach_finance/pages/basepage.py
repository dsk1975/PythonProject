from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = None
        self.wait = None

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self, title):
        self.get_wait().until(EC.title_is(title))
        return self.driver.title

    def get_wait(self):
        if self.wait:
            return self.wait
        self.wait = WebDriverWait(self.driver, 4)
        return self.wait

    def is_visible(self, locator):
        try:
            self.get_wait().until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_clickable(self, locator):
        try:
            self.get_wait().until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator):
        self.get_wait().until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self, locator, text):
        self.get_wait().until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        element = self.get_wait().until(EC.visibility_of_element_located(locator))
        return element.text

    def scroll_to_bottom(self,locator):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")