from tests.unit.unit_base_test import UnitBaseTest
from models.user import UserModel


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel("Username", "password")

        self.assertEqual("Username", user.username)
        self.assertEqual("password", user.password)
