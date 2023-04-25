# Write a function that takes two numbers as input and returns their sum.

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))


def sum_of_two_numbers(a, b):
    return a + b

result = sum_of_two_numbers(x, y)
print(f"The sum of {x} and {y} is {result}")
