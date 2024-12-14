# Lesson 6: Lists and Tuples
# This lesson covers:
# - List creation and access
# - List methods (append, insert, remove, etc.)
# - List slicing
# - Tuples and their immutability
# - List comprehensions

def main():
    # List creation and access
    fruits = ["apple", "banana", "orange", "grape"]
    print("Original list:", fruits)
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])

    # List methods
    print("\nList Methods:")
    fruits.append("mango")
    print("After append:", fruits)
    
    fruits.insert(1, "kiwi")
    print("After insert:", fruits)
    
    fruits.remove("banana")
    print("After remove:", fruits)
    
    popped_fruit = fruits.pop()
    print("Popped fruit:", popped_fruit)
    print("After pop:", fruits)

    # List slicing
    print("\nList Slicing:")
    numbers = [0, 1, 2, 3, 4, 5]
    print("Original numbers:", numbers)
    print("First three:", numbers[:3])
    print("Last three:", numbers[-3:])
    print("Every second number:", numbers[::2])

    # Tuples
    print("\nTuples:")
    coordinates = (10, 20)
    print("Coordinates:", coordinates)
    x, y = coordinates  # tuple unpacking
    print(f"X: {x}, Y: {y}")

    # List comprehension
    print("\nList Comprehension:")
    squares = [n**2 for n in range(5)]
    print("Squares:", squares)
    
    even_numbers = [n for n in range(10) if n % 2 == 0]
    print("Even numbers:", even_numbers)


if __name__ == "__main__":
    main() 