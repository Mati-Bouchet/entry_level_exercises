# Write a function that takes two arguments (a and b) and returns the result of dividing a by b.

x = int(input("Please enter a number: "))

y = int(input("Please enter another number: "))

def divide_by(a, b):
    if b == 0:
        return ZeroDivisionError("You cannot divide a number by zero. Please choose a different number.")
    else:
        return a / b

result = divide_by(x, y)

print(result)