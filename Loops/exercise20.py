# Take a series of number by input, convert it into a list and show in consolo the sum of all numbers greater than 10
list =  input("Please enter a list of numbers separated by a space: ").split()

list_conv = [int(i) for i in list]

total_sum = 0

for i in list_conv:
    if i >= 10:
        total_sum += i
        
print(total_sum)