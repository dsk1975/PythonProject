import json
import requests
import pytest
import pytest_html



class TestApi:
    url = 'http://api.coindesk.com/v1/bpi/currentprice.json'

    def test_call_api(self):
        response = requests.request('GET', TestApi.url)
        response_dict = response.json()
        assert response_dict['disclaimer'] == \
               'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org'
        return response_dict
        # print(response_dict)
    @pytest.mark.api
    def test_status_code(self):

        response_two = requests.request('GET', TestApi.url)
        assert response_two.status_code == 200