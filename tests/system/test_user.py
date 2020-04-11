from tests.base_test import BaseTest
from models.user import UserModel
import json


class UserSystemTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():  # in this project this initializes db
                response = client.post("/register", data={"username": "test", "password": "abc"})

                self.assertEqual(201, response.status_code)
                self.assertDictEqual({"id": 1, "username": "test"}, response.json)
                self.assertIsNotNone(UserModel.find_by_username("test"))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():  # in this project this initializes db
                client.post("/register", data={"username": "test", "password": "abc"})
                auth_response = client.post(
                    "/auth",
                    data=json.dumps({"username": "test", "password": "abc"}),
                    headers={"Content-Type": "application/json"}
                )

                self.assertEqual(200, auth_response.status_code)
                self.assertIn('access_token', auth_response.json.keys())

    def test_register_duplicate_user(self):
        with self.app() as client:
            with self.app_context():  # in this project this initializes db
                client.post("/register", data={"username": "test", "password": "abc"})
                response = client.post("/register", data={"username": "test", "password": "abc"})

                self.assertEqual(response.status_code, 400)
