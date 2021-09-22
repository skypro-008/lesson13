import json
import unittest

from task import app


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_gt(self):
        with app.app_context():
            address = "/get_tickets?price=gt:19000"
            app.testing = True
            response = app.test_client().get(address)
        self.assertEqual(response.status_code, 200, msg="Не правильно работает фильтрация gt:19000")
        response_json = json.loads(response.data)
        self.assertEqual(response_json, [
            {
                "from": {
                    "country": "Russia",
                    "airport": "DME",
                },
                "to": {
                    "country": "USA",
                    "airport": "LAX",
                },
                "price": 78634,
                "available": True,
                "date": "2011-03-16",
            },
            {
                "from": {
                    "country": "Russia",
                    "airport": "SVO",
                },
                "to": {
                    "country": "USA",
                    "airport": "ATL",
                },
                "price": 87909,
                "available": False,
                "date": "2011-03-14",
            }
        ])

    def test_lt(self):
        with app.app_context():
            address = "/get_tickets?price=lt:87909"
            app.testing = True
            response = app.test_client().get(address)
        self.assertEqual(response.status_code, 200, msg="Не правильно работает фильтрация gt:19000")
        response_json = json.loads(response.data)
        self.assertEqual(response_json, [
            {
                "from": {
                    "country": "Russia",
                    "airport": "DME",
                },
                "to": {
                    "country": "USA",
                    "airport": "LAX",
                },
                "price": 78634,
                "available": True,
                "date": "2011-03-16",
            },
            {
                "from": {
                    "country": "Russia",
                    "airport": "VKO",
                },
                "to": {
                    "country": "USA",
                    "airport": "ORD",
                },
                "price": 19000,
                "available": True,
                "date": "2011-02-11",
            },
        ])
