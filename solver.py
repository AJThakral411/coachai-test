import math


def average(numbers):
    if not numbers:
        raise ValueError("average() needs at least one number")
    return sum(numbers) / len(numbers)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    if abs(math.cos(math.radians(degrees))) < 1e-12:
        raise ValueError(f"tan({degrees:g}) is undefined")
    return math.tan(math.radians(degrees))


ONE_NUMBER_OPERATIONS = {"sin": sine, "cos": cosine, "tan": tangent}


def ask_number(prompt):
    """Keep asking until the user types a number (or q to quit)."""
    while True:
        text = input(prompt).strip()
        if text.lower() == "q":
            return None
        try:
            return float(text)
        except ValueError:
            print("That's not a number. Try again.")


def ask_operator():
    """Keep asking until the user types + - * / sin cos tan (or q to quit)."""
    while True:
        op = input("Operator (+ - * / sin cos tan): ").strip().lower()
        if op == "q":
            return None
        if op in OPERATIONS or op in ONE_NUMBER_OPERATIONS:
            return op
        print("Please type one of + - * / sin cos tan")


def main():
    print("Simple Calculator (type q at any time to quit)")
    print("For sin, cos and tan, the first number is the angle in degrees.")
    while True:
        a = ask_number("First number: ")
        if a is None:
            break
        op = ask_operator()
        if op is None:
            break
        if op in ONE_NUMBER_OPERATIONS:
            try:
                result = round(ONE_NUMBER_OPERATIONS[op](a), 12) + 0.0
                print(f"{op}({a:g}) = {result:g}")
            except ValueError as error:
                print(f"Error: {error}")
            continue
        b = ask_number("Second number: ")
        if b is None:
            break
        try:
            result = OPERATIONS[op](a, b)
            print(f"{a:g} {op} {b:g} = {result:g}")
        except ZeroDivisionError as error:
            print(f"Error: {error}")
    print("Goodbye!")


if __name__ == "__main__":
    main()
