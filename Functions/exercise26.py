# Use map() and filter() together to square all the odd numbers in a list.

number_list = input("Please enter a list of numbers separated by a space: ").split()

number_list = [int(i) for i in number_list]

def sqr_odd_numbers(ite):
    filtered_list = list(filter(lambda x : x % 2 != 0, ite))
    sqrd_list = list(map(lambda x : x ** 2, filtered_list))
    return sqrd_list

final_list = sqr_odd_numbers(number_list)
print(final_list)