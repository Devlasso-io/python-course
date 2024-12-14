# Lesson 0: Print Basics
# This lesson covers:
# - Basic print statement
# - Print with different data types
# - Print with multiple arguments
# - Print formatting


def main():
    # Simple print statement
    print("Hello, welcome to Python!")

    # Print with different data types
    print(42)  # printing numbers
    print(3.14)  # printing floating point numbers
    print(True)  # printing boolean values

    # Print with multiple arguments
    print("Number:", 42, "Pi:", 3.14)

    # Print with different separators
    print("Python", "is", "awesome", sep=" -> ")

    # Print with different end characters
    print("This line doesn't end with newline", end="")
    print("so this appears on the same line")


if __name__ == "__main__":
    main()
