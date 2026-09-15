"""
Program 6: Recursive string reversal
Concept: Recursion - string manipulation
"""

def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s: Input string
        
    Returns:
        Reversed string
        
    Base case: Empty string or single character returns itself
    Recursive step: reverse_string(s) = reverse_string(s[1:]) + s[0]
    """
    # Base case
    if len(s) <= 1:
        return s
    
    # Recursive step
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    # Test with 'hello'
    test_string = "hello"
    result = reverse_string(test_string)
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{result}'")
    print("Expected: 'olleh'")
    
    # Additional test cases
    print(f"\nReverse of 'a': '{reverse_string('a')}'")  # Should be 'a'
    print(f"Reverse of '': '{reverse_string('')}'")      # Should be ''
    print(f"Reverse of 'world': '{reverse_string('world')}'")  # Should be 'dlrow'