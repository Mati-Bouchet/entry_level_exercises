n = int(input("Enter number: ")) # 5
f = 1


if(n == 0 or n < 0):
    print("Value of n should be greater than 1")
else:
    for i in range (1, n+1, 1):
        f *= i
        print(f)