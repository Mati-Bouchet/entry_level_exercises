# Write a Python program to count the frequency of each element in a list.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 6, 5, 1, 2, 2, 3, 7]

def count_freq(ite):
    freq_list = {}
    for i in ite:
        if i in freq_list:
            freq_list[i] += 1
        else:
            freq_list[i] = 1
    return freq_list
    
result = count_freq(number_list)

print(result)


