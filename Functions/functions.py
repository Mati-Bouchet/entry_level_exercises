
name = input("Please enter your name \n")
age = input("And what's your age?\n")

def hello(name, age):  # If we don't pass an argument here, you can add a default, optional parameter that will take in place
    print(f"Hello, {name}! You are {age} years old")


hello(name, age)
