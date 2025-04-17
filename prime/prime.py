"""Module implementing functions that determine if a number is prime or not.

A prime number is one that that is divisible only by 1 and itself. If
a number is divisible by any other number (other than 1 or itself), it
is a composite number (not prime).

Interesting things to think about:

Is a negative number prime?

How can we reduce the number of checks needed to figure out if a
number is prime or not? Do we really need to check all possible
numbers between 1 and the number?
"""

def is_prime(num):
    """Returns True if |num| is prime, and False if it isn't.

    num: int

    returns: bool
    """
    return False

def run():
    num = input("Please enter a number: ")
    p = "" if is_prime(year) else "NOT"
    print(f"{num} is {p} a prime number")

if __name__ == '__main__':
    run()
