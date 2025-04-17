import unittest
from leap_year import is_leap_year

class Testing(unittest.TestCase):
    def test_is_leap_year(self):
        self.assertEqual(is_leap_year(2000), True)
        self.assertEqual(is_leap_year(1900), False)
        self.assertEqual(is_leap_year(2004), True)
        self.assertEqual(is_leap_year(2001), False)

if __name__ == '__main__':
    unittest.main()
