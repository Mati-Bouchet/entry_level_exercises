# Write a program that counts the vowels in a String

word = input("Please enter a word: ")
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0

for i in word:
    if i.lower() in vowels:
        vowel_count += 1
        
print(f"{word} has {vowel_count} vowel(s)")