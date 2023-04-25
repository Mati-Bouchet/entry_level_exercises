# Find out wheter a number is prime or not

num = int(input("Please enter a number to determine if it is prime or not: "))

if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print("This number is not prime")
            break
        else:
            print("This number is prime")
            break