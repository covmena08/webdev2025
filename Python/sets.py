# Adding items to a dictionary
my_dict = {'name': 'Alice', 'age': 25}
my_dict['city'] = 'New York'  # Add new key-value pair
print("After adding:", my_dict)

# Removing items from a dictionary
removed_value = my_dict.pop('age')  # Remove by key
print("After removing 'age':", my_dict)
del my_dict['city']  # Remove using del
print("After deleting 'city':", my_dict)

# Looping through a dictionary
person = {'name': 'Bob', 'age': 30, 'city': 'London'}
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# Copy items in a dictionary
person_copy = person.copy()
print("Copied dictionary:", person_copy)

# Nested dictionaries
students = {
    'student1': {'name': 'John', 'age': 20},
    'student2': {'name': 'Jane', 'age': 22}
}
print("Nested dictionary:", students)
for student_id, info in students.items():
    print(f"{student_id}: Name={info['name']}, Age={info['age']}")