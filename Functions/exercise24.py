from functools import reduce  
# Use reduce() to calculate the product of all the numbers in a list.

number_list = input("Please enter a list of numbers separated by a space: ").split()

number_list = [int(i) for i in number_list]

def product_of_list(ite):
    return reduce(lambda a, b:  a * b, ite)
    

print(product_of_list(number_list))