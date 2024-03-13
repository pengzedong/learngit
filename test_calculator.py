# test_calculator.py

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

if __name__ == '__main__':
    unittest.main()