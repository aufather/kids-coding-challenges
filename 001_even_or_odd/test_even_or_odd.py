import unittest
from even_or_odd import is_even, is_odd

class Testing(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(is_even(0), True)
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(3), False)

    def test_is_odd(self):
        self.assertEqual(is_odd(0), False)
        self.assertEqual(is_odd(1), True)
        self.assertEqual(is_odd(2), False)
        self.assertEqual(is_odd(3), True)

if __name__ == '__main__':
    unittest.main()
