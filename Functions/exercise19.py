# Write a function that takes a list of strings as input and returns a new list with all the strings that have more than three characters converted to uppercase. Use a nested function to check the length of each string and to convert a string to uppercase.

str_list = input("Please enter a list of words: ").split()

def convert_upper(list1):
    def is_long_enough(word):
        return len(word) > 3
    def to_upper(word):
        return word.upper()
    filtered_list = list(filter(is_long_enough, list1))  # Filter is a function that applies to each element of an iterable and returns the elements if true.
    upper_list = list(map(to_upper, filtered_list)) # Map is a function that works as an iterator to return a result after applying a function to every item of an iterable.
    return upper_list

result = convert_upper(str_list)

print(result)