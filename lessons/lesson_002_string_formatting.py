# Lesson 2: String Formatting
# This lesson covers:
# - String concatenation
# - F-strings
# - Format method
# - String operations

def main():
    name = "Python"
    version = 3.12
    
    # String concatenation
    print("Basic concatenation: " + name + " version " + str(version))
    
    # F-strings (recommended)
    print(f"Using f-strings: {name} version {version}")
    
    # Format method
    print("Using format method: {} version {}".format(name, version))
    
    # String operations
    print("\nString operations:")
    text = "python programming"
    print("Uppercase:", text.upper())
    print("Capitalize:", text.capitalize())
    print("Title case:", text.title())
    print("Replace:", text.replace("python", "Python"))


if __name__ == "__main__":
    main() 