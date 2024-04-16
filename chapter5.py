# Chapter 5: Control Flow in Python

# 5.1 Conditional Statements
age = 18
if age < 18:
    print("You're a minor.")
elif age >= 18 and age < 21:
    print("You're an adult, but not of legal drinking age.")
else:
    print("You're an adult and of legal drinking age.")

# 5.2 Loops
# Example: for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example: while loop
count = 0
while count < 5:
    print(count)
    count += 1

# 5.3 Break and Continue
# Example: break
for i in range(10):
    if i == 5:
        break
    print(i)  # Output: 0 1 2 3 4

# Example: continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Output: 1 3 5 7 9

# 5.4 Nested Loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
# Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)