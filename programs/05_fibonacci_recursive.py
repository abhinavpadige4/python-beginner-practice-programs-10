"""
Program 5: Recursive Fibonacci (nth term)
Concept: Recursion - Fibonacci sequence
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        nth Fibonacci number
        
    Base cases:
        fibonacci(0) = 0
        fibonacci(1) = 1
    Recursive step:
        fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # Test with Fibonacci of 7 (should be 13)
    n = 7
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
    print("Expected: 13")
    
    # Show first few Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}", end=" ")
    print()