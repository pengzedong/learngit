import unittest
from user_account import UserAccount

class TestUserAccount(unittest.TestCase):
    
    def setUp(self):
        UserAccount.users = []

    def test_unique_id(self):
        UserAccount("John Doe", "password123", "user_001", "john@example.com")
        with self.assertRaises(ValueError):
            UserAccount("Jane Doe", "password456", "user_001", "jane@example.com")

if __name__ == '__main__':
    unittest.main()
