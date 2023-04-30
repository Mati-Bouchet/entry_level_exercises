# Use filter() to remove all the even numbers from a list.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def remove_even(ite):
    filtered_list = list(filter(lambda x : x % 2 != 0, ite))
    return filtered_list

no_even_list = remove_even(number_list)

print(no_even_list)
