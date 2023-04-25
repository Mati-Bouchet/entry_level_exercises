# Write a function that takes two arguments (a and b) and returns their product.

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

def product_of(a, b):
    return a*b

result = product_of(x, y)

print(f"The product of {x} and {y} is {result}")