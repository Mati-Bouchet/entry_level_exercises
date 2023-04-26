# Write a function that takes a list of dictionaries, each containing a "name" key and an "age" key, as input and returns the name of the oldest person in the list. Use a nested function to extract the age from each dictionary.

people = [
{"name": "Joan", "age": 25},
{"name": "Pedro", "age": 36},
{"name": "Linda", "age": 31},
]

def get_oldest_perdon(people_list):
    def get_age(age):
        return age["age"]
    oldest_person = max(people_list, key = get_age)
    return oldest_person["name"]

result = get_oldest_perdon(people)
print(result)