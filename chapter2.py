# Chapter 2: Python Syntax and Data Types

# 2.1 Python Syntax
# Indentation
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Comments
# This is a single-line comment

"""
This is a
multi-line
comment.
"""

# Variables
my_variable = 42
print(my_variable)  # Output: 42

# 2.2 Python Data Types
# Numbers
int_value = 42
float_value = 3.14
complex_value = 2 + 3j

print(int_value)  # Output: 42
print(float_value)  # Output: 3.14
print(complex_value)  # Output: (2+3j)

# Strings
string_value = "Hello, world!"
print(string_value)  # Output: Hello, world!

# Booleans
bool_value = True
print(bool_value)  # Output: True

# Lists
list_value = [1, 2, 3, 4, 5]
print(list_value)  # Output: [1, 2, 3, 4, 5]

# Tuples
tuple_value = (1, 2, 3)
print(tuple_value)  # Output: (1, 2, 3)

# Dictionaries
dict_value = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(dict_value)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Sets
set_value = {1, 2, 3, 4, 5}
print(set_value)  # Output: {1, 2, 3, 4, 5}