# Write a recursive function to check if a string is a palindrome.

word = input("Please enter a word yo check if it's a palindrome: ")

def is_palindrome(w):
    if len(w) <= 1:
        return True
    else:
        if w[0].lower() == w[-1].lower():
            return is_palindrome(w[1:-1])
        else:
            return False
        
result = is_palindrome(word)
print(result)
