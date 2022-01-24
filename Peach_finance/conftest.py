import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    # if request.param == 'firefox':
    #     driver = webdriver.Firefox(GeckoDriverManager().install())

        request.cls.driver = driver
        driver.implicitly_wait(10)
        yield
        driver.quit()