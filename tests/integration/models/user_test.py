from models.user import UserModel
from tests.base_test import BaseTest


class UserIntegrationTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            user = UserModel("un", "abc")

            self.assertIsNone(UserModel.find_by_username("un"))
            self.assertIsNone(UserModel.find_by_id(1))

            user.save_to_db()

            self.assertIsNotNone(UserModel.find_by_username("un"))
            self.assertIsNotNone(UserModel.find_by_id(1))