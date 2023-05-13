# Write a Python program that creates a dictionary where the keys are strings and the values are lists of strings. The program should allow the user to add new values to existing keys or create new keys.

dict = {
    "Fruits": ["apple", "orange", "pineapple"],
    "Colors": ["blue", "red", "yellow"],
    "Animals": ["cat", "dog", "lizard"],
}

key = input("Please enter a key for the dictionary: ")


values = input("Enter the value(s) for the corresponding key, separated by commas: ".format(key)).split(",")

if key in dict:
    dict[key].extend(values)
else:
    dict[key] = values


print(dict)