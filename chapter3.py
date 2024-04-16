# Chapter 3: Working with Python Data Types

# 3.1 Numbers
x = 5
y = 3
print(x + y)  # Output: 8
print(x - y)  # Output: 2
print(x * y)  # Output: 15
print(x / y)  # Output: 1.6666666666666667
print(abs(-7))  # Output: 7
print(pow(2, 3))  # Output: 8
print(round(3.14159, 2))  # Output: 3.14

# 3.2 Strings
name = "Alice"
greeting = "Hello, " + name + "!"
print(greeting)  # Output: Hello, Alice!

message = "The quick brown fox jumps over the lazy dog."
print(message[4:9])  # Output: quick

age = 30
print("My name is {} and I'm {} years old.".format(name, age))
# Output: My name is Alice and I'm 30 years old.

# 3.3 Lists
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing list elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry

# Modifying list elements
fruits[1] = "orange"
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# List methods
fruits.append("grape")
print(fruits)  # Output: ['apple', 'orange', 'cherry', 'grape']