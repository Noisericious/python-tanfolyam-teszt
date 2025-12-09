import unittest

from egységtesztek.user_manager import UserManager


class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()
        self.manager.add_user("Elek")
        self.manager.add_user("Alex")

    def tearDown(self):
        self.manager = None

    def test_add_user(self):
        self.manager.add_user("Mari")
        self.assertIn("Mari", self.manager.get_users())

    def test_remove_user(self):
        self.manager.remove_user("Elek")
        self.assertNotIn("Elek", self.manager.get_users())

    def test_get_users(self):
        users = self.manager.get_users()
        self.assertEqual(users, ["Alex", "Elek"])

if __name__ == '__main__':
    unittest.main()

