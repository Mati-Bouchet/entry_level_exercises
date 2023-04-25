words = input("Please enter a list of words separated by a space: ").split()

list = [str(i) for i in words]

vowels = ["a", "e", "i", "o", "u"]

count = 0

for i in list:
    if i[0].lower() in vowels:
        count +=1
        print(i)

print(count)