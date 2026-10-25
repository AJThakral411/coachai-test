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
    """Keep asking until the user types + - * / (or q to quit)."""
    while True:
        op = input("Operator (+ - * /): ").strip()
        if op.lower() == "q":
            return None
        if op in OPERATIONS:
            return op
        print("Please type one of + - * /")


def main():
    print("Simple Calculator (type q at any time to quit)")
    while True:
        a = ask_number("First number: ")
        if a is None:
            break
        op = ask_operator()
        if op is None:
            break
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
