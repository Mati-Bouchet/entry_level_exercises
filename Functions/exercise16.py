#  Write a function that takes a string as input and returns the string with all vowels removed. Use a nested function to check if a character is a vowel.

word_input = input("Please enter a word: ")

vowel_list = ["a", "e", "i", "o", "u;"]

def remove_vowel(word):

    def is_vowel(char):
        for i in char:
            if i.lower() in vowel_list:
                return True
    result = ""
    for i in word:
        if not is_vowel(i):
            result += i
    return result

final = remove_vowel(word_input)

print(final)