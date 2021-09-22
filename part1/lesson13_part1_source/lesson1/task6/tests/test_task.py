import json
import unittest

from task import app


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_get_user(self):
        with app.app_context():
            address = "/get_user/1"
            app.testing = True
            response = app.test_client().get(address)
        self.assertEqual(response.status_code, 200, msg="bad request")
        response_json = json.loads(response.data)
        self.assertEqual(response_json, {
            "id": 1,
            "name": "Ivan",
            "age": 34,
            "is_blocked": False
        })

    def test_get_users(self):
        with app.app_context():
            address = "/get_users"
            app.testing = True
            response = app.test_client().get(address)
        self.assertEqual(response.status_code, 200, msg="bad request")
        response_json = json.loads(response.data)
        self.assertEqual(response_json, [
            {
                "id": 1,
                "name": "Ivan",
                "age": 34,
                "is_blocked": False
            },
            {
                "id": 2,
                "name": "Peter",
                "age": 23,
                "is_blocked": True
            }
        ], msg="Ошибка получения всех пользователей - не те пользователи")

    def test_create_user(self):
        with app.app_context():
            address = "/create_user"
            app.testing = True
            response = app.test_client().post(address, json={
                "id": 3,
                "name": "Maxim",
                "age": 90,
                "is_blocked": False
            })
        self.assertEqual(response.status_code, 201, msg="Ошибка создания пользователя")
