# Write a function that takes a list of numbers as input and returns the largest number in the list

numbers = input("Please enter a list of numbers separated by a space: ").split()

numbers = [int(i) for i in numbers]



def largest_number(list):
    comparator = list[0]
    for i in list:
        if i > comparator:
            comparator = i

    return comparator

larg_num = largest_number(numbers)

print(f"The largest number in the list is {larg_num}")