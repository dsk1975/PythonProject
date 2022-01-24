import pytest
import requests
import json

class TestCatApi:
    url = 'https://cat-fact.herokuapp.com/facts'

    def test_cat_api(self):

        responce = requests.request("GET", TestCatApi.url)
        resp = responce.json()
        print(resp)
        assert responce.status_code == 200
        assert resp['_id'] == '5887e1d85c873e0011036889'