# Chapter 4: Advanced Python Data Types

# 4.1 Dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary elements
print(person["name"])  # Output: Alice
print(person.get("age"))  # Output: 30

# Modifying dictionary elements
person["age"] = 31
person["country"] = "USA"
print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# Dictionary methods
print(person.keys())  # Output: dict_keys(['name', 'age', 'city', 'country'])
print(person.values())  # Output: dict_values(['Alice', 31, 'New York', 'USA'])
print(person.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York'), ('country', 'USA')])

# 4.2 Sets
fruits = {"apple", "banana", "cherry"}
vegetables = {"carrot", "spinach", "broccoli"}

# Set operations
print(fruits | vegetables)  # Union: {'banana', 'cherry', 'apple', 'broccoli', 'carrot', 'spinach'}
print(fruits & vegetables)  # Intersection: set()
print(fruits - vegetables)  # Difference: {'banana', 'cherry', 'apple'}

# Adding and removing elements
fruits.add("grape")
fruits.remove("banana")
print(fruits)  # Output: {'grape', 'cherry', 'apple'}

# 4.3 Tuples
point = (2, 3)
print(point[0])  # Output: 2
print(point[1])  # Output: 3

# Unpacking tuples
x, y = point
print(x)  # Output: 2
print(y)  # Output: 3