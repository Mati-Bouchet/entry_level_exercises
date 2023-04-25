num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))

if num1 > num2 and num1 > num3:
    print(f"The first number, {num1}, is the maximum number")
elif num2 > num1 and num2 > num3:
    print(f"The second number, {num2}, is the maximum number")
else:
    print(f"The third number, {num3}, is the maximum number")