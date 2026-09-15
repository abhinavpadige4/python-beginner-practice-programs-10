"""
Program 8: Count word frequencies in a sentence using a dictionary
Concept: Dictionaries - counting with dictionaries
"""

def count_word_frequencies(sentence):
    """
    Count the frequency of each word in a sentence using a dictionary.
    
    Args:
        sentence: Input string
        
    Returns:
        Dictionary with words as keys and their frequencies as values
    """
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Initialize empty dictionary for word counts
    word_count = {}
    
    # Count each word
    for word in words:
        # Remove punctuation from the word
        cleaned_word = word.strip('.,!?;:"()[]{}')
        if cleaned_word:  # Only count non-empty words
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
    
    return word_count

def print_word_frequencies(word_count):
    """Print word frequencies in a formatted way."""
    print("Word Frequencies:")
    print("-" * 20)
    for word, count in sorted(word_count.items()):
        print(f"'{word}': {count}")

if __name__ == "__main__":
    # Test with sample input: 'test test demo'
    test_sentence = "test test demo"
    result = count_word_frequencies(test_sentence)
    
    print(f"Input sentence: '{test_sentence}'")
    print_word_frequencies(result)
    print()
    print(f"Expected: {{'test': 2, 'demo': 1}}")
    print(f"Actual:   {result}")
    
    # Additional test
    print("\n" + "="*40)
    test_sentence2 = "Hello world hello Python world"
    result2 = count_word_frequencies(test_sentence2)
    print(f"Input sentence: '{test_sentence2}'")
    print_word_frequencies(result2)