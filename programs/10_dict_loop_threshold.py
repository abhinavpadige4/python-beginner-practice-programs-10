"""
Program 10: Loop over dictionary to find keys with values above threshold
Concept: Dictionaries - looping through dictionaries
"""

def find_keys_above_threshold(scores, threshold):
    """
    Find all keys in a dictionary where the value is above a given threshold.
    
    Args:
        scores: Dictionary with keys and numeric values
        threshold: Numeric threshold value
        
    Returns:
        List of keys where values are above the threshold
    """
    keys_above_threshold = []
    
    # Loop through dictionary items
    for key, value in scores.items():
        if value > threshold:
            keys_above_threshold.append(key)
    
    return keys_above_threshold

def find_keys_above_threshold_v2(scores, threshold):
    """
    Alternative implementation using list comprehension.
    
    Args:
        scores: Dictionary with keys and numeric values
        threshold: Numeric threshold value
        
    Returns:
        List of keys where values are above the threshold
    """
    return [key for key, value in scores.items() if value > threshold]

if __name__ == "__main__":
    # Test with sample dictionary of scores
    test_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96,
        "Eve": 83,
        "Frank": 79
    }
    
    threshold = 80
    
    print("Student Scores:")
    print("-" * 20)
    for name, score in test_scores.items():
        print(f"{name}: {score}")
    print()
    
    # Find students with scores above threshold
    result = find_keys_above_threshold(test_scores, threshold)
    result_v2 = find_keys_above_threshold_v2(test_scores, threshold)
    
    print(f"Students with scores > {threshold}:")
    print(f"Method 1 (loop): {result}")
    print(f"Method 2 (list comprehension): {result_v2}")
    print()
    print("Expected: ['Alice', 'Bob', 'Diana', 'Eve'] (order may vary)")
    
    # Additional test with different threshold
    print("\n" + "="*40)
    threshold2 = 90
    result2 = find_keys_above_threshold(test_scores, threshold2)
    print(f"Students with scores > {threshold2}: {result2}")
    print("Expected: ['Bob', 'Diana']")
    
    # Show the actual scores for verification
    print("\nVerification:")
    for student in result2:
        print(f"{student}: {test_scores[student]} (>{threshold2})")