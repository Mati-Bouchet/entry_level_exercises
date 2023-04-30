# Write a recursive function to find the length of a string.

word = input("Please enter a word to find its length: ")

def word_length(w):
    if not w:
        return 0
    else:
        return 1 + word_length(w[1:])
    
result = word_length(word)
print(f"Total characters: {result}")