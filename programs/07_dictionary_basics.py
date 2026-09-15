"""
Program 7: Dictionary basics - create, access, update, delete a student record
Concept: Dictionaries - basic operations
"""

def demonstrate_dictionary_basics():
    """Demonstrate basic dictionary operations: create, access, update, delete."""
    
    # Create a student record dictionary
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "is_full_time": True
    }
    
    print("Initial student record:")
    print(student)
    print()
    
    # Access values
    print("Accessing values:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"GPA: {student['gpa']}")
    print()
    
    # Update values
    print("Updating values:")
    student["age"] = 21  # Update age
    student["gpa"] = 3.9  # Update GPA
    student["year"] = "Junior"  # Add new key-value pair
    print(f"Updated student: {student}")
    print()
    
    # Delete values
    print("Deleting values:")
    removed_major = student.pop("major", "Not found")  # Remove and return value
    print(f"Removed major: {removed_major}")
    print(f"Student after removing major: {student}")
    print()
    
    # Check if key exists
    print("Checking key existence:")
    print(f"Has 'email' key: {'email' in student}")
    print(f"Has 'name' key: {'name' in student}")
    
    # Get all keys and values
    print(f"\nAll keys: {list(student.keys())}")
    print(f"All values: {list(student.values())}")

if __name__ == "__main__":
    demonstrate_dictionary_basics()