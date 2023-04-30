# Write a recursive function to calculate the factorial of a number.

number = int(input("Please enter a number to calculate its factorial: "))

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
    
result = fact(number)
print(result)