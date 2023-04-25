# Write a function that takes a list of numbers as input and returns the average of those numbers.

numbers = input("Enter a list of numbers separated by a space: ").split()

numbers = [int(i) for i in numbers]

def average_number(list):
    if len(list) == 0:
        return None
    else:
        return sum(list) / len(list)


average = average_number(numbers)

print(average)