# Write a function that takes a list of strings as input and returns a new list with all the strings converted to uppercase.

list_of_strings = input("Please enter a list of words separated by a space: ").split()


def all_upper_case(words):
    uppercase_list = []
    for i in words:
        i = i.upper()
        uppercase_list.append(i)
    return uppercase_list
        



convert = all_upper_case(list_of_strings)

print(convert)