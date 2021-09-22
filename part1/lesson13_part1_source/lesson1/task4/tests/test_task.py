import json
import unittest

from task import app


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_get_user(self):
        with app.app_context():
            address = "/salary/32?name=artur"
            app.testing = True
            response = app.test_client().get(address)
        self.assertEqual(response.status_code, 200, msg="bad request")
        response_json = json.loads(response.data)
        self.assertEqual(response_json.get("name"), "artur")
        self.assertEqual(response_json.get("salary"), 32)