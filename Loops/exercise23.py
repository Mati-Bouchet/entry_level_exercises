#  Write a program that takes a list of strings as input from the user and prints the length of the longest string in the list.

list = input("Please enter a list of words separated by a space: ").split()

word_length = 0

for i in list:
    if len(i) > word_length:
        word_length = len(i)


print(f"The length of the longest string in the list is {word_length}")


