from functools import reduce
# Use reduce() to concatenate all the strings in a list.

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def concatenated_str(ite):
    concatenated_list = reduce(lambda x, y : x + y, ite)
    return concatenated_list

print(concatenated_str(week_days))