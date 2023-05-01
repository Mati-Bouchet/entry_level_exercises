# Write a recursive function to find the greatest common divisor of two numbers.

num = int(input("Please enter a number: "))

num2 = int(input("Please enter a second number: "))

def greatest_common_divisor(x, y):
    if y == 0:
        return x
    else:
        return greatest_common_divisor(y, x % y)
    
result = greatest_common_divisor(num, num2)
print(result)