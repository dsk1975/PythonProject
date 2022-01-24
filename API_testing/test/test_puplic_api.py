import json
import requests
import pytest
import pytest_html


# class TestPuplicAPI:
#     """
#
#     """
#     def test_create_booking(self):
#         url = 'https://restful-booker.herokuapp.com/booking/'
#
#         payload = json.dumps({
#             "firstname": "Jim",
#             "lastname": "Brown",
#             "totalprice": 111,
#             "depositpaid": True,
#             "bookingdates": {
#                 "checkin": "2018-01-01",
#                 "checkout": "2019-01-01"
#             },
#             "additionalneeds": "Breakfast"
#         })
#         headers = {
#             'Content - type': 'application/json'
#         }
#         response = requests.request("POST", url, headers=headers, data=payload)
#         print(response)
#         print(response.status_code)
#         assert response.json()['booking']['firstname'] == 'Jim'



# pytest -m marker_name + folder name /



