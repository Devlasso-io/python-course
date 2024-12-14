# Lesson 3: Operators in Python
# This lesson covers:
# - Arithmetic operators (+, -, *, /, //, %, **)
# - Comparison operators (==, !=, >, <, >=, <=)
# - Logical operators (and, or, not)
# - Assignment operators (=, +=, -=, etc.)

def main():
    # Arithmetic operators
    print("Arithmetic Operators:")
    a, b = 10, 3
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Floor Division: {a} // {b} = {a // b}")
    print(f"Modulus: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")

    # Comparison operators
    print("\nComparison Operators:")
    x, y = 5, 5
    print(f"Equal to: {x} == {y} is {x == y}")
    print(f"Not equal to: {x} != {y} is {x != y}")
    print(f"Greater than: {x} > {y} is {x > y}")
    print(f"Less than: {x} < {y} is {x < y}")

    # Logical operators
    print("\nLogical Operators:")
    is_sunny = True
    is_warm = True
    print(f"is_sunny AND is_warm: {is_sunny and is_warm}")
    print(f"is_sunny OR is_warm: {is_sunny or is_warm}")
    print(f"NOT is_sunny: {not is_sunny}")


if __name__ == "__main__":
    main() 