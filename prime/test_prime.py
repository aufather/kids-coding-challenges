import unittest
from prime import is_prime

class Testing(unittest.TestCase):
    def test_is_prime(self):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
        for i in range(30):
            self.assertEqual(is_prime(i), i in primes, msg=f"Failed for num = {i}")

        for i in range(-1, -10, -1):
            self.assertEqual(is_prime(i), i in primes, msg=f"Failed for num = {i}")

if __name__ == '__main__':
    unittest.main()
