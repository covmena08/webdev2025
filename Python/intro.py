
print("Hello Python world")

#This is a single line comment

"""
This is a multi-line comment"""

#Indentation is important in Python
# The following code will not work:
# if True:
#     print("This will not work")
if True:
    print("This will work")
print("No indentation here")
#    print("This is a single indentation. This will not work either")  # This line is incorrectly indented because it is not aligned with the previous print statement

if 10>5:
    print("10 is greater than 5")

#Python identifiers
# An identifier is a name given to entities like class, functions, variables, module or other objects. 
# It helps to differentiate one entity from another.  
# Rules for writing identifiers:
# 1. An identifier names can start with letters in lowercase (a to z), uppercase (A to Z), or an underscore (_) followed by either numbers, letters, underscores etc.. 
#    Example: my_variable, _myVariable, MyVariable1
# 2. An identifier cannot START with a digit digits (0 to 9), but can contain digits after the first character.
#    Example: 1myVariable is not valid, but myVariable1 is valid.
# 3. An identifier can only contain alphanumeric characters and underscores but not special characters like @, $, %, etc.
#    Invalid identifiers: my-variable, my variable, because it contains a hyphen and space which are considered special characters.
# 4. An identifier cannot be a RESERVED KEYWORD in Python (like if, else, while, for, return, def, class, break, continue, True, False, None, and, as, include, import, from, del etc.). 
# 5. Identifiers are case-sensitive, meaning that 'myVariable' and 'myvariable' would be considered different identifiers.

counter = 100 # Declaring a variable in Python. This creates an integer value (a positive/negative whole number)
kilometer = 12.65 # Floating point variable/value (a number with a decimal point)
myNme = "Kenneth Kaunda" # String variable (a sequence of characters)

"""
# The Python interpreter automatically infers the datatype of variable based on the value assigned to it.
print(counter)
print(kilometer)
print(myNme)

# Deleting a variable in Python
# del variable_name (in case of single variable), # del variable_name1, variable_name2, variable_nameN (in case of multiple variables)
del counter # This will delete the variable 'counter' 
"""
# Displaying the datatype of a variable
print (type(kilometer))  # This will display the type of the variable 'kilometer'
print (type(myNme))  # This will display the type of the variable 'my
print (type(counter))  # This will display the type of the variable 'counter'

# Casting Python variables
# Casting is the process of converting a variable from one datatype to another.
# In Python, you can cast variables using the int(), float(), str() functions.
x = str(counter)  # Convert 'counter' to a string
y = float(2)
print(x)  # This will print the value of 'x' 
print(type(x))  # This will print the type of 'x' which is now a string
print (y)  # This will print the value of 'y'
print(type(y))  # This will print the type of 'y' which is a float

#Multiple variable assignment
# Instead of:
a = 10
b = 10
c = 10
a = b = c = 10  # This will assign the value 10 to variables a, b, and c
# print(a, b, c)  # This will print the values of a, b, and c
# You can also assign different values to multiple variables in one line
x, y, z = 1, 2.5, "Hello"  # This will assign 1 to x, 2.5 to y, and "Hello" to z even if they are of different datatypes
# print(x, y, z)  # This will print the values of x, y, and z
# Python allows you to use single quotes OR double quotes for strings

# Cases:
# camel Case: myVariableName
# Pascal Case: MyVariableName
# snake_case: my_variable_name
# kebab-case: my-variable-name (not allowed in Python identifiers)

# Local and Global Variables
# A local variable is a variable that is defined within a function and can only be accessed within that function.
def my_function(x, y):
    local_var = x + y  # This is a local variable, defined within the function
    return local_var
print(my_function(5, 10)) # This will print the result of the function, which is 15
# However, if you try to access 'local_var' outside of the function, it will raise an error
# print(local_var)  # This will raise an error because 'local_var' is not defined outside of the function


# A Global variable is a variable that is defined outside of any function and can be accessed from anywhere in the code.
r = 23 # This is a global variable, defined outside of any function
s = 32 # Global variable

def new_function():
    diff= s-r # This is a local variable, defined within the function
    return diff  # This will return the value of 'diff' which is 9
print(new_function())  # This will print the result of the function, which is 9

PI_VALUE = 3.14  # This is a constant variable because it is written in uppercase letters
# Constants are usually defined in uppercase letters to differentiate them from regular variables.