"""Implements a function to find the nth number in fibonacci sequence.

Fibonacci numbers are formed by adding the previous two numbers in the
sequence. The first two numbers in the sequence is 1, 1. The sequence is
+-------+---------+-------+
| Index | formula | value |
+-------+---------+-------+
|     1 |         |     1 |
+-------+---------+-------+
|     2 |         |     1 |
+-------+---------+-------+
|     3 +   1 + 1 |     2 |
+-------+---------+-------+
|     4 |   2 + 1 |     3 |
+-------+---------+-------+
|     5 |   3 + 2 |     5 |
+-------+---------+-------+
|     6 |   5 + 3 |     8 |
+-------+---------+-------+
...
"""

def fibo(index):
    """Returns the fibonacci number at |index|.

    index: int

    return: int
    """
    return -1

def run():
    index = int(input("Please enter the index: "))
    f = fibo(index)
    print(f"Fibonacci number at index {index} is {f}")

if __name__ == '__main__':
    run()
