# Write a function that takes a string as input and returns True if the string is a palindrome (reads the same backwards as forwards) and False otherwise.

word = input("Please enter a word: ")


def is_palindrome(w):
    if w.lower() == w.lower()[::-1]:
        return True
    else:
        return False
    
check_palindrome = is_palindrome(word)

print(check_palindrome)
