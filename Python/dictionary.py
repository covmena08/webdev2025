# Dictionary is mutable, that is, we can change (update, adde, remove) the values of a dictionary after it has been created.
capitals= {"Kenya": "Nairobi", "China": "Beijing", "Chile": "Santiego", "Thailand":"Bangkok", "Japan": "Tokyo"}
numbers= {1: "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"}
score={"Jane":79, "Maria": 88, "Smith": 67, "Andrew": 77, "Jonathan":90}


# print(captitals)
# print(numbers)
# print(score)

#dict1= {["Mango, "Apple", "Banana"]: "Fruit", "Vegetable" [Carrot, "Potato", "Onion"]}
#print(dict1) # This will throw an error because we're using immutable elements (elements of a list) within a mutable dictionary. The dictionary can't work with immutable elements.

# Accessing elements within a dictionary
# Square Bracket Notation
print(capitals["Kenya"]) # You can use the keyname from the key-value pair or an index number
# OR
firstCapital= capitals["Kenya"]
print("The Kenyan capital is:", firstCapital)

# get() method
print(capitals.get("China"))
# OR
secondCapital= capitals.get("China")
print("The Chinese capital is:", secondCapital)
# Remove, modify and iterate through elements in a dictionary
# Assignment: read and implement examples on adding items, removing items, loops, copy items, and the use of nested dictionaries.

# Adding items to a dictionary
capitals= {"Kenya": "Nairobi", "China": "Beijing", "Chile": "Santiego", "Thailand":"Bangkok", "Japan": "Tokyo"}
capitals["USA"] ="Washington"
print("After adding:", capitals)

# Updating items in a dictionary
capitals["USA"]="Washington DC"
print("After update:", capitals)

# Removing items from a Dictionary
# We can remove items from dictionary using the following methods:
# del keyword: Removes an item by key.
# pop() method: Removes an item by key and returns its value.
# clear() method: Empties the dictionary.
# popitem() method: Removes and returns the last key-value pair.

del capitals["Chile"]
# OR
capitals.pop("Thailand")
print("After removing:", capitals)

# Looping through capitals
# We can iterate over keys [using keys() method] , values [using values() method] or both [using item() method] with a for loop.
# Iterate over keys
for key in capitals:
    print("The keys in capitals are:", key)
# Iterate over values
for value in capitals.values():
    print("The values in capitals are:", value)
# Iterate over key-value pairs
for key, value in capitals.items():
    print(f"{key}: {value}")

# Copying a dictionary with copy() method
import copy
capitals_copy = copy.deepcopy(capitals)
print(capitals)
print("Copied capitals:", capitals_copy)

# Nested dictionaries example
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print("Enrolled students' details:", students)
