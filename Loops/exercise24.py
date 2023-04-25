#  Write a program that takes a list of numbers as input from the user and prints the sum of all the even numbers in the list.

nums= input("Please enter a list of numbers separated by a space: ").split()

nums = [int(i) for i in nums]

sum = 0

for i in nums:
    if i % 2 != 0:
        sum += i

print(f"The sum of all even numbers is {sum}")
