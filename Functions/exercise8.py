# Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.

numbers = input("Please enter a list of numbers separated by a space: ").split()

numbers = [int(i) for i in numbers]

def sun_of_numbers(nums):
    return sum(nums)

result = sun_of_numbers(numbers)
print(f"The sum of the numbers typed in is {result}")