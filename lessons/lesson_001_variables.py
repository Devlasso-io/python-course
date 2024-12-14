# Lesson 1: Variables and Basic Data Types
# This lesson covers:
# - Variable declaration
# - Basic data types
# - Type conversion
# - Variable naming rules

def main():
    # Variable declaration and basic types
    message = "Hello, Python!"  # str
    number = 42                 # int
    pi = 3.14159               # float
    is_python_fun = True       # bool
    
    # Printing variables
    print("String variable:", message)
    print("Integer variable:", number)
    print("Float variable:", pi)
    print("Boolean variable:", is_python_fun)
    
    # Type conversion
    number_as_string = str(number)
    string_as_number = int("123")
    
    print("\nType conversion examples:")
    print(f"Number {number} converted to string: {number_as_string}")
    print(f"String '123' converted to number: {string_as_number}")


if __name__ == "__main__":
    main() 