# Write a function that takes a list of numbers as input and returns the sum of all the even numbers in the list. Use a nested function to check if a number is even.

list_input = input("Please enter a list of numbers separated by a space: ").split()

list_input = [int(i) for i in list_input]


def sum_of_numbers(list):
    def is_even(number):
        if number % 2 == 0:
            return True
    even_sum = 0
    for i in list:
        if is_even(i):
            even_sum += i
    return even_sum



result = sum_of_numbers(list_input)

print(f"The sum of all even numbers is {result}")
