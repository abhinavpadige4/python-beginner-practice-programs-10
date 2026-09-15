"""
Program 4: Recursive factorial function
Concept: Recursion - base case and recursive step
"""

def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n (n!)
        
    Base case: factorial(0) = 1
    Recursive step: factorial(n) = n * factorial(n-1)
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive step
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test with factorial of 5
    num = 5
    result = factorial(num)
    print(f"Factorial of {num} = {result}")
    print("Expected: 120")
    
    # Additional test cases
    print(f"Factorial of 0 = {factorial(0)}")  # Should be 1
    print(f"Factorial of 3 = {factorial(3)}")  # Should be 6