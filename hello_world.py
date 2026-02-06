# Simple Hello World Program with Basic Logic

# Hello World
print("Hello, World!")

# Simple Logic - Check if number is even or odd
number = 10
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

# Simple Logic - Calculate sum of numbers
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Sum of {numbers} is {total}")

# Simple Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
