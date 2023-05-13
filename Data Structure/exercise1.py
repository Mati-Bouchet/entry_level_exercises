# Write a Python program to create a list of tuples, where each tuple contains the name and age of a person. Sort the list by age in ascending order.

list_of_people = [
    ("Lisa", 28),
    ("John", 22),
    ("Joseph", 64),
    ("Elizabeth", 35),
]

def sort_people(ite):
    ite.sort(key=lambda person : person[1])
    for i in ite:
        print(i)

sorted_list = sort_people(list_of_people)
print(sorted_list)