# Write a function that takes a list of strings as input and returns a new list with all the strings sorted in alphabetical order.

list1 = input("Please enter a list of words separated by a space: ").split()

def sort_by_az(list):
    list2 = []
    for i in list:
        list2.append(i)
    list2.sort()
    return list2

sorted_list = (sort_by_az(list1))

print(sorted_list)