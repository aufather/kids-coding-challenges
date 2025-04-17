"""Evaluate a simple expression of the form num1 operand num2.

|num1| and |num2| are integers. While |operand| is a string of these values
'+', '-', '*', '/', or '%'. The function evaluate should return the
resulting value of evaluating num1 operand num2.
"""

def evaluate(num1, operand, num2):
    """Evaluates a simple expression num1 operand num2 and returns the result.

    num1: int
    operand: str
    num2: int

    returns: int
    """
    return 0

def run():
    num1, operand, num2 = input("Please enter an expression: ").split()
    value = evaluate(num1, operand, num2)
    print(f"{num1} {operand} {num2} = {value}")

if __name__ == '__main__':
    run()
