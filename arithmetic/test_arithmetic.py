import unittest
from arithmetic import evaluate

class Testing(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate(1, "+", 2), 3)
        self.assertEqual(evaluate(1, "+", 0), 1)
        self.assertEqual(evaluate(0, "+", 2), 2)
        self.assertEqual(evaluate(1, "+", -1), 0)
        self.assertEqual(evaluate(2, "+", -1), 1)
        self.assertEqual(evaluate(1, "+", -2), -1)
        self.assertEqual(evaluate(-2, "+", -1), -3)
        self.assertEqual(evaluate(-2, "+", 1), -1)

    def test_subtraction(self):
        self.assertEqual(evaluate(2, "-", 1), 1)
        self.assertEqual(evaluate(1, "-", 0), 1)
        self.assertEqual(evaluate(0, "-", 2), -2)
        self.assertEqual(evaluate(1, "-", -1), 2)
        self.assertEqual(evaluate(2, "-", -1), 3)
        self.assertEqual(evaluate(1, "-", -2), 3)
        self.assertEqual(evaluate(-2, "-", -1), -1)
        self.assertEqual(evaluate(-2, "-", 1), -3)

    def test_multiplication(self):
        self.assertEqual(evaluate(2, "*", 1), 2)
        self.assertEqual(evaluate(2, "*", 6), 12)
        self.assertEqual(evaluate(1, "*", 0), 0)
        self.assertEqual(evaluate(0, "*", 2), 0)
        self.assertEqual(evaluate(2, "*", -2), -4)
        self.assertEqual(evaluate(-2, "*", -3), 6)

    def test_division(self):
        self.assertEqual(evaluate(2, "/", 1), 2)
        self.assertEqual(evaluate(6, "/", 2), 3)
        self.assertEqual(evaluate(2, "/", -2), -1)
        self.assertEqual(evaluate(-6, "/", -3), 2)
        self.assertEqual(evaluate(0, "/", 2), 0)
        self.assertRaises(ZeroDivisionError, lambda: evaluate(2, "/", 0))

    def test_modulo(self):
        self.assertEqual(evaluate(6, "%", 4), 2)
        self.assertEqual(evaluate(2, "%", 2), 0)
        self.assertEqual(evaluate(2, "%", 1), 0)
        self.assertEqual(evaluate(-6, "%", 3), 0)
        self.assertEqual(evaluate(-6, "%", -3), 0)
        self.assertEqual(evaluate(0, "%", 2), 0)
        self.assertRaises(ZeroDivisionError, lambda: evaluate(2, "%", 0))

if __name__ == '__main__':
    unittest.main()
