"""
    In Python, errors are often used for flow controls,
    very much like if statements.
"""


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Dividend cannot be Zero.")

    return dividend / divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [99, 77]},
]

print("Welcome to the average grade program.")
try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    # Runs here if ZeroDivisionError clause is true
    print("There are no grades yet in your list.")
else:
    # Runs here if try clause is true
    print(f"The average grade is {average}")
finally:
    # finally clause always runs
    print("Thank You!")
