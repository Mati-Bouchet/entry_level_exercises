# Write a function that takes a string as input and returns the string reversed.

word = input("Please enter a word: ")

def reversed_str(a):
    return a[::-1]

reverse = reversed_str(word)
print(reverse)