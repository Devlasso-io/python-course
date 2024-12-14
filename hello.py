# Lesson 1: Introduction to Python Basics
# This is a simple Python program that demonstrates:
# - Functions
# - Print statements
# - Program entry points

def main():
    # The print() function displays text to the console
    print("Welcome to the Python Learning Course!")
    print("Let's learn Python step by step!")
    
    # Demonstrate basic string usage
    course_name = "Python Fundamentals"
    lesson_number = 1
    print(f"You are in {course_name}, Lesson {lesson_number}")


# This is a special condition that checks if this file is run directly
# (rather than being imported as a module)
if __name__ == "__main__":
    main()
