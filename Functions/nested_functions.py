def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')  # split is used to separate string in different units, using as rule the argument we pass in it. In this case, a space
    for word in words:
        say(word)


talk("Hola Don Pepito")

def counter():
    count = 0

    def increment ():
        nonlocal count
        count = count + 1
        return count 

    return increment

increment = counter()

print(increment())
print(increment())
print(increment())
print(increment())