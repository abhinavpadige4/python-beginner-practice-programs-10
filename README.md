# Python Beginner Practice Programs - 10 Programs

This repository contains 10 Python practice programs designed for beginners to learn and practice:
- Loops (for/while, nested loops)
- Recursion (base case, recursive step)
- Dictionaries (creation, access, update, deletion, nesting)

## Programs Included

### 1. **01_print_numbers.py** - Simple for-loop
**Concept**: Loops - for loop
**Description**: Print numbers from 1 to 10 using a for loop
**Output**: Numbers 1 through 10, each on a new line

### 2. **02_sum_while.py** - While-loop sum
**Concept**: Loops - while loop
**Description**: Compute the sum of a list of integers using a while loop
**Test**: Input [5, 10, 15] → Output: 30

### 3. **03_multiplication_table.py** - Nested loops
**Concept**: Loops - nested for loops
**Description**: Print a 10x10 multiplication table using nested for loops
**Output**: Formatted multiplication table from 1×1 to 10×10

### 4. **04_factorial_recursive.py** - Recursive factorial
**Concept**: Recursion - base case and recursive step
**Description**: Calculate factorial of a number using recursion
**Test**: factorial(5) → Output: 120

### 5. **05_fibonacci_recursive.py** - Recursive Fibonacci
**Concept**: Recursion - Fibonacci sequence
**Description**: Calculate the nth Fibonacci number using recursion
**Test**: fibonacci(7) → Output: 13

### 6. **06_reverse_string_recursive.py** - Recursive string reversal
**Concept**: Recursion - string manipulation
**Description**: Reverse a string using recursion
**Test**: "hello" → Output: "olleh"

### 7. **07_dictionary_basics.py** - Dictionary basics
**Concept**: Dictionaries - basic operations
**Description**: Create, access, update, and delete a student record dictionary
**Operations**: Create record, access values, update values, delete keys

### 8. **08_word_frequency.py** - Word frequency counter
**Concept**: Dictionaries - counting with dictionaries
**Description**: Count word frequencies in a sentence using a dictionary
**Test**: "test test demo" → Output: {'test': 2, 'demo': 1}

### 9. **09_nested_dict_inventory.py** - Nested dictionary inventory
**Concept**: Dictionaries - nested dictionaries
**Description**: Manage product inventory with nested dictionaries (price, stock, category)
**Operations**: View inventory, access product info, update stock, add new products

### 10. **10_dict_loop_threshold.py** - Dictionary looping with threshold
**Concept**: Dictionaries - looping through dictionaries
**Description**: Find keys in a dictionary where values are above a threshold
**Test**: Given scores dict, find keys with score > 80

## How to Run

Each program is a standalone Python file. To run any program:

```bash
python programs/01_print_numbers.py
```

Replace the program number as needed (01 through 10).

To run all programs sequentially:
```bash
for i in {01..10}; do
    echo "Running program $i:"
    python programs/${i}_*.py
    echo "---"
done
```

## Requirements

- Python 3.8+

## Topics Covered

### **Loops**
- for loops: iterating over ranges
- while loops: conditional repetition
- nested loops: loops inside loops (multiplication table)

### **Recursion**
- base cases: stopping conditions for recursive functions
- recursive steps: function calling itself with modified parameters
- examples: factorial, Fibonacci sequence, string reversal

### **Dictionaries**
- creation: defining key-value pairs
- access: retrieving values using keys
- update: modifying existing values or adding new keys
- deletion: removing key-value pairs
- nesting: dictionaries within dictionaries
- looping: iterating through keys, values, or items
- applications: counting, inventory management, threshold filtering

## Learning Path

The programs progress from simple to more complex concepts:

1. **Basic loops** (programs 1-3): Introduction to for and while loops
2. **Recursion fundamentals** (programs 4-6): Understanding base cases and recursive steps
3. **Dictionary operations** (programs 7-10): From basic CRUD operations to nested structures and practical applications

Each program includes clear comments explaining the concept being demonstrated and validation test cases.

## GitHub Repository Structure

```
python-beginner-practice-programs-10/
├── .gitignore              # Git ignore file for Python
├── README.md               # This file
└── programs/
    ├── 01_print_numbers.py
    ├── 02_sum_while.py
    ├── 03_multiplication_table.py
    ├── 04_factorial_recursive.py
    ├── 05_fibonacci_recursive.py
    ├── 06_reverse_string_recursive.py
    ├── 07_dictionary_basics.py
    ├── 08_word_frequency.py
    ├── 09_nested_dict_inventory.py
    └── 10_dict_loop_threshold.py
```

## Validation

Each program has been tested and includes validation code that runs when the script is executed directly. The expected outputs are shown in the comments and validation sections of each program.

Happy coding! 🐍