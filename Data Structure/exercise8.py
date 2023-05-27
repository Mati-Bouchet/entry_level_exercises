# Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.

students_names = {"Student 1": "Steve", "Student 2": "Arnold", "Student 3": "Elizabeth", "Student 4": "Xavier"}

def sort_students(ite):
    return sorted(ite.values())

print(sort_students(students_names))