numbers = input("Enter a list of numbers separated by a space: ").split()

numbers = [int(i) for i in numbers]

largest_num = numbers[0]

for i in numbers:
    if i > largest_num:
        largest_num = i

print(f"The largest number is {largest_num}")