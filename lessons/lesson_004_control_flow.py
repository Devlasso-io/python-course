# Lesson 4: Control Flow
# This lesson covers:
# - If statements
# - If-else statements
# - If-elif-else chains
# - Nested conditions

def main():
    # Simple if statement
    age = 18
    if age >= 18:
        print("You are an adult")

    # If-else statement
    temperature = 25
    if temperature > 30:
        print("It's hot outside!")
    else:
        print("The temperature is pleasant")

    # If-elif-else chain
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Your grade is: {grade}")

    # Nested conditions
    is_weekend = True
    is_sunny = True
    if is_weekend:
        if is_sunny:
            print("Let's go to the beach!")
        else:
            print("Let's watch a movie at home")
    else:
        print("It's a work day")


if __name__ == "__main__":
    main() 