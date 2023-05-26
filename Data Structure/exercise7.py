# Write a Python program that creates a set of integers and removes all the even numbers from it.


set_of_int = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

def remove_even(ite):
    new_set = {1}
    for i in ite:
        if i % 2 != 0:
            new_set.add(i)
    return new_set

print(remove_even(set_of_int))