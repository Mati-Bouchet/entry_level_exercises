# Write a function that takes a list of numbers as input and returns a new list with all the numbers squared. Use a nested function to calculate the square of a number.

from cmath import sqrt


number_list = input("Please enter a list of numbers: ").split()

number_list = [int(i) for i in number_list]

def sqr_list(list1):
    def get_sqr(number):
        return number ** 2
    squared_list = list(map(get_sqr, list1)) # Map is a function that works as an iterator to return a result after applying a function to every item of an iterable.
    return squared_list

result = sqr_list(number_list)

print(result)
