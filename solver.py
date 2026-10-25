def average(numbers):
    if not numbers:
        raise ValueError("average() needs at least one number")
    return sum(numbers) / len(numbers)
