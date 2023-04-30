# Write a recursive function to reverse a string.

word = input("Please enter a word to reverse it: ")

def reverse(w):
    if len(w) == 0:
        return w
    else:
        return reverse(w[1:]) + w[0]
    
reversed_word = reverse(word)
print(reversed_word)