# Write a function that takes a list of numbers as input and returns the sum of the squares of all even numbers in the list. Use a nested function to check if a number is even.

number_list = input("Please enter a list of numbers: ").split()

number_list = [int(i) for i in number_list]

def sum_square_even(list1):
    def is_even(number):
        return number % 2 == 0
    sum_of_sqrs = 0
    for i in list1:
        if is_even(i):
            sum_of_sqrs += i ** 2
    return sum_of_sqrs

result = sum_square_even(number_list)

print(result)