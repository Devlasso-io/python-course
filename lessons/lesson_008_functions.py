# Lesson 8: Functions
# This lesson covers:
# - Function definition and calling
# - Parameters and arguments
# - Return values
# - Default parameters
# - *args and **kwargs
# - Lambda functions

def greet(name):
    """Simple function with one parameter"""
    return f"Hello, {name}!"

def calculate_total(prices, discount=0):
    """Function with default parameter"""
    total = sum(prices)
    return total * (1 - discount)

def print_info(*args, **kwargs):
    """Function demonstrating *args and **kwargs"""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

def main():
    # Basic function calls
    print("Basic Functions:")
    message = greet("Python Learner")
    print(message)

    # Function with default parameter
    print("\nUsing Default Parameters:")
    prices = [10, 20, 30]
    total = calculate_total(prices)
    print(f"Total without discount: ${total}")
    
    total_with_discount = calculate_total(prices, 0.1)
    print(f"Total with 10% discount: ${total_with_discount}")

    # Using *args and **kwargs
    print("\nVariable Arguments:")
    print_info(1, 2, 3, name="John", age=25)

    # Lambda functions
    print("\nLambda Functions:")
    square = lambda x: x**2
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(square, numbers))
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared}")

    # Function as argument
    def apply_operation(func, value):
        return func(value)

    print("\nFunction as Argument:")
    double = lambda x: x * 2
    result = apply_operation(double, 5)
    print(f"Double of 5: {result}")


if __name__ == "__main__":
    main() 