# Lesson 5: Loops
# This lesson covers:
# - While loops
# - For loops
# - Loop control statements (break, continue)
# - Range function
# - Nested loops

def main():
    # While loop
    print("While Loop Example:")
    count = 0
    while count < 3:
        print(f"Count is: {count}")
        count += 1

    # For loop with range
    print("\nFor Loop with Range:")
    for i in range(3):
        print(f"Iteration {i}")

    # For loop with string
    print("\nIterating over a string:")
    for char in "Python":
        print(char, end=" ")
    print()  # New line

    # Break statement
    print("\nBreak Example:")
    for i in range(5):
        if i == 3:
            break
        print(i, end=" ")
    print()

    # Continue statement
    print("\nContinue Example:")
    for i in range(5):
        if i == 2:
            continue
        print(i, end=" ")
    print()

    # Nested loops
    print("\nNested Loops:")
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")


if __name__ == "__main__":
    main() 