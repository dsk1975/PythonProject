import pytest
from test_api import TestApi


class TestDataFromApi(TestApi):

    text = 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org'

    @pytest.mark.api
    def test_use_api(self):
        data = self.test_call_api()
        assert TestDataFromApi.text in data['disclaimer']