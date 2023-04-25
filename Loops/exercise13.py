# Python program to print a multiplication table of a given number

num = int(input("Please enter a number: "))

for i in range(1, 11, 1):
    result = num * i
    print(f"5 x {i} = {result}")
