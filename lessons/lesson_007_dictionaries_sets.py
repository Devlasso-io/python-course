# Lesson 7: Dictionaries and Sets
# This lesson covers:
# - Dictionary creation and access
# - Dictionary methods
# - Sets and their operations
# - Set methods
# - Common use cases

def main():
    # Dictionary creation and access
    student = {
        "name": "John",
        "age": 20,
        "grades": {"math": 90, "science": 85}
    }
    
    print("Dictionary Basics:")
    print("Student:", student)
    print("Name:", student["name"])
    print("Math grade:", student["grades"]["math"])

    # Dictionary methods
    print("\nDictionary Methods:")
    print("Keys:", student.keys())
    print("Values:", student.values())
    
    # Using get() with default value
    print("History grade:", student.get("history", "Not enrolled"))
    
    # Adding and updating
    student["email"] = "john@example.com"
    student["age"] = 21
    print("Updated student:", student)

    # Sets
    print("\nSets:")
    fruits = {"apple", "banana", "orange"}
    vegetables = {"carrot", "lettuce", "banana"}
    
    print("Fruits:", fruits)
    print("Vegetables:", vegetables)

    # Set operations
    print("\nSet Operations:")
    print("Union:", fruits | vegetables)
    print("Intersection:", fruits & vegetables)
    print("Difference (fruits - vegetables):", fruits - vegetables)
    
    # Set methods
    fruits.add("grape")
    print("After adding grape:", fruits)
    
    fruits.remove("apple")
    print("After removing apple:", fruits)


if __name__ == "__main__":
    main() 