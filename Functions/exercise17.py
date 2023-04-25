# Write a function that takes a list of strings as input and returns a new list with all the strings sorted in descending order of length. Use a nested function to get the length of each string.

string_list = input("Please enter a list of strings: ").split()

def sorted_list(list):
    def get_string_length(string):
            return len(string)
    string_list2 = sorted(list, key=get_string_length, reverse=True)
    return string_list2

descending_list = sorted_list(string_list)

print(descending_list)