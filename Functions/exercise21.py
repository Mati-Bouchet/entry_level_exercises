# Write a function that takes a list of strings as input and returns a new list with all the strings that have more than two vowels. Use a nested function to check the number of vowels in each string.

word_list = input("Please insert a list of words: ").split()

vowels = ["a", "e", "i", "o", "u"]

def words_with_two_vowels(list_input):
    def count_vowels(word):
        count = 0
        for i in word:
            if i.lower() in vowels:
                count += 1
        return count
    filtered_list = []
    for i in list_input:
        if count_vowels(i) > 2:
            filtered_list.append(i)
    return filtered_list

result = words_with_two_vowels(word_list)

print(result)
