import unittest
from fibonacci import fibo

class Testing(unittest.TestCase):
    def test_fibo(self):
        fibos = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
        for i in range(1, len(fibos) + 1):
            self.assertEqual(fibo(i), fibos[i - 1], msg=f"Failed for index = {i}")

if __name__ == '__main__':
    unittest.main()
