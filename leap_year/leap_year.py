"""Implements function that determine if a year is leap year or not.

A leap year has an extra day compared to a non leap year. So it has
366 days instead of 365 days. The extra day is February, 29.

A year is a leap year if
 * it is divisible by 400
 * or it is divisible by 4 but not by 100

All other years are not leap years.
"""

def is_leap_year(year):
    """Returns True if |year| is a leap year. Returns False otherwise.

    year: int

    return: bool
    """
    return False

def run():
    year = input("Please enter a year: ")
    leap = "" if is_leap_year(year) else "NOT"
    print(f"{year} is {leap} a leap year")

if __name__ == '__main__':
    run()
