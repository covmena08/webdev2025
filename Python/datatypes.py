#Datatypes;
#Numeric Datatypes: integers, floating, complex numbers
intNum=10 # Integer
floatNum=10.5 # Float= floating point number is a number with a decimal point
complexNum=3+5j # Complex number is a number with a real and imaginary part, represented as a + bj where a is the real part and b is the imaginary part
# Boolean Datatype: True or False
boolNum=True # Boolean (True/False)
# Checking the type of a variable in terminal
print("The type of value stored in intNum variable:", intNum, "is", type(intNum))
print("The type of value stored in complexNum variable:", complexNum, "is", type(complexNum))


#String Datatype: sequence of characters
strNum = "NextStep" 
strNum2= 'NextStep' 
strNum3= '''NextStep 
is 
offering a web dev course
this 
summer
''' 
# output: NextStep, NextStep, NextStep is offering a web dev course this summer
# String can be defined using single quotes, double quotes, or triple quotes for multi-line strings

#print(strNum2)
#print(strNum3)
# Displaying the string variable in different ways
print(strNum) # Prints the complete string
print(strNum[0]) # Prints the first character of the string
print(strNum[1:5]) # Prints characters from index 1 to 4 (not including 5)
print(strNum[1:]) # Prints characters from index 1 to the end of the string
print(strNum[:5]) # Prints characters from the start to index 4 (not including 5)
print(strNum[-1]) # Prints the last character of the string
print(strNum[1:5:2]) # Prints characters from index 1 to 4 with a step of 2 (i.e., every second character)
print(strNum * 2) # Prints the string twice
print(strNum + " Organization") # Concatenates two strings

#Python Sequence Datatypes: list, tuple, range
# List: A list is a collection of items that can be of different datatypes, defined using square brackets []. Like an array in js
firstList= ['abcd', 856, 2.456, True] # A list can contain different datatypes
secondList= ['John', 456] # Another list with different items

# A few operations on lists
#print(firstList)  # Prints the whole first list
#print(firstList[0])  # Prints the first item of the first list
#print(firstList[1:4])  # Prints items from index 1 to 3 (not including 4)
#print(firstList[2:])  # Prints items from index 3 to the end of the list
#print(firstList[:3])  # Prints items from the start to index 2 (not including 3)
#print(firstList[-1])  # Prints the last item of the first list
#print(firstList[1:4:2])  # Prints items from index 1 to 3 with a step of 2 (i.e., every second item)
#print(firstList * 3)  # Prints the first list three times
#print(firstList + secondList)  # Concatenates the first and second lists
# A list can hold another list as an item
#thirdList = [firstList, secondList]  # This creates a list containing the first

# TupleS: A tuple is similar to a list but is immutable (cannot be changed meaning that items cannot be added to or removed from tuples, and items cannot be replaced within tuples), defined using parentheses (). Like an array in js. It can hold different datatypes even a list or another tuple
firstTuple = ('abcd', 8246, 2.546, True, [23, 56, "List in a tuple"])  # A tuple can contain different datatypes
secondTuple = ('Mary', 496, ('road', 24323, "Tuple in a tuple"))  # Another tuple with different items
# A few operations on tuples
#print(firstTuple)  # Prints the whole first tuple
#print(firstTuple[0])  # Prints the first item of the first tuple
#print(firstTuple[1:4])  # Prints items from index 1 to 3
#print(firstTuple[2:])  # Prints items from index 3 to the end of the tuple
#print(firstTuple[:3])  # Prints items from the start to index 2
#print(firstTuple[-1])  # Prints the last item of the first tuple
#print(firstTuple[1:4:2])  # Prints items from index 1 to 3 with a step of 2 (i.e., every second item)
#print(firstTuple * 3)  # Prints the first tuple three times
# print(firstTuple + secondTuple)  # Concatenates the first and second tuples

#Python Range Datatype: range
# A range is a sequence of numbers, often used in loops. It can be defined using the range() function.
# Syntax: range(start, stop, step)    start specifies the starting number, stop specifies the end number (not included), and step specifies the increment/decrement between numbers (optional)
#Examples
# for i in range(5):  # This will print numbers from 0 to 4
#    print(i)  #Prints numbers from 0 to 4 in separate lines
#    print(i, end=' ')  # Prints numbers from 0 to 4 in the same line separated by space
# for i in range(2, 10):  # This will print numbers from 2 to 9
#    print(i, end=' ')  # Prints numbers from 2 to 9 in the same line separated by space
# for i in range(2, 10, 2):  # This will print even numbers from 2 to 8
#    print(i, end=' ')  # Prints even numbers: 2, 4, 6, 8 in the same line separated by space
# Note: The range() function returns a range object, which is an immutable sequence type.


# Binary Datatype: A binary datatype is a sequence of bits (0s and 1s) that can represent data in a computer. In Python, binary data can be represented using the bytes type.
#Bytes: A bytes object is an immutable sequence of bytes, which can be used to represent binary data. It is defined using the b prefix before a string literal.
# Bytes datatypes: each byte is represented by an integer value between 0 and 255 received as a network packet or read from a file. ASCII (American Standard Code for Information Interchange) is a character encoding standard that uses 7 bits to represent characters, allowing for 128 different characters. In Python, bytes can be created using the bytes() constructor or by prefixing a string with b.
# Using the bytes() cunstructor/function to create bytes objects
# value= bytes([65, 66, 67, 68, 69])  # Creates a bytes object with the values 65, 66, and 67
# print(value) # Prints the bytes object

# value2= b'Hello'  # b is a prefix that automatically creates a bytes object with the string 'Hello'
# print(value2)  # Prints the bytes object
value3 = bytearray([72, 101, 108, 108, 111])  # Creates a mutable bytes object with the values 72, 101, 108, 108, and 111
# print(value3)  # Prints the bytearray object

# Python Dictionary Datatype: A dictionary is a collection of key-value pairs, defined using curly braces {}. It is an unordered collection of items where each item is stored as a pair of keys and values.
dict = {} # Creating an empty dictionary
dict2 = {'name': 'John', 'age': 30, 'city': 'New York'}  # Creating a dictionary with key-value pairs
# A few operations on dictionaries
print(dict2)  # Prints the whole dictionary
print(dict2['name'])  # Prints the value associated with the key 'name'
print(dict2.keys()) # Prints all the keys in the dictionary
print(dict2.values()) # Prints all the values in the dictionary

# Python Set Datatype: A set is an unordered collection of unique items, defined using curly braces {} or the set() constructor. It is similar to a mathematical set and does not allow duplicate items.
set1 = {1, 2, 3, 4, 5, 5}  # Creating a set with unique items (duplicates are removed by the interpreter)
set2 = {'Html', 'Css', 'JavaScript', 'Python', 'php', 'perl', 'c'}  # Creating a set with string items
print(set1)  # Prints the whole set

# Boolean Datatype: A boolean datatype can have only two values: True or False. It is often used in conditional statements and logical operations.
boolVar = True  # Creating a boolean variable with the value True
print(boolVar)
print(type(boolVar))  # Prints the type of the boolean variable, which is <class 'bool'>

b=10
print(bool(b))
c=() # Empty tuple
print(bool(c))  # Prints False because an empty tuple is considered False in a boolean context

d=None  # None is a special constant in Python that represents the absence of a value or a null value
print(bool(d))  # Prints False because None is considered False in a boolean context
print(type(d))  # Prints the type of None, which is <class 'NoneType'>
# None is often used to indicate that a variable has no value or that a function does not return a value.



















3