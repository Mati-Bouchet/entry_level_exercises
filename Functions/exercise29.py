# Write a recursive function to find the sum of all the elements in a list.

number_list = input("Please enter a list of numbers separated by a space: ").split()

number_list = [int(i) for i in number_list]

def sum(ite):
    if not ite:
        return 0
    else:
        return ite[0] + sum(ite[1:])
    
result = sum(number_list)
print(result)