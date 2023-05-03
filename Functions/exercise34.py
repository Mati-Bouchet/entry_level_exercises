# Write a function that returns the division of two numbers. Make sure one of the numbers is not 0 by using a decorator

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

def check_if_zero(func):
    def check(a, b):
        if b == 0:
            print("Can't divide by zero")
        else:
            func(a, b)
    return check

@check_if_zero
def div(a, b):
    print(a / b)

div(num1, num2)


