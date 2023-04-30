# Use map() to square all the numbers in a list.

number_list = input("Please enter a list of numbers separated by a space: ").split()

number_list = [int(i) for i in number_list]

def square(ite):
    new_number_list = list(map(lambda a : a ** 2, ite))
    return new_number_list

print(square(number_list))
