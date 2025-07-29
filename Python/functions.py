# Functions
#Syntax:
# def functionName(parameters):
#    "function_docstring" # Optional, it describes what the function does
#    code to be executed
#    return [expression] # Optional, it returns a value from the function. Expression is in square brackets because it is optional

#Simple Python Function
def greet():
    "This function prints a greeting message"
    print("Hello, welcome to the world of Python functions!")  # Print a greeting message
    return
greet()  # Call the greet function to execute it in terminal


def testFunction(param):
    print("ID inside the function", id(param))  # Print the memory address(=where variable is stored) of the parameter passed to the function
    return
varTest= "Hello, Developer?"
print("ID before passing: ", id(varTest))  # Print the memory address of the variable before calling the function
testFunction(varTest)  # Call the testFunction with varTest as an argument

# Python function arguements
# Function with one argument. This function takes a single parameter and prints a message with that parameter.
def greetings(developerName):
    "Greets the person whose name is passed as an argument"
    print("Hello, {}! Welcome to the world of Python functions!".format(developerName))  # Print a greeting message with the developer's name
    return
greetings("Lenin")  # Call the greetings function with "Lenin" as an argument
greetings("Natarah")
greetings("Anina")
greetings("Theresa")
#the parameter is a placeholder for the value that will be passed to the function when it is called. In this case, `developerName` is the parameter that will hold the name of the developer eg "Lenin" when the function is called.
# Positional or required arguements: These are the arguments that must be provided in the correct order when calling the function. The values passed to these arguments are assigned to the corresponding parameters in the function definition.
def positional(str):
    "This function prints a passed string into it"
    print()  
    return
#Call the positional function with a string argument
# positional() # If arguement is not passed, it will raise an error: TypeError: positional() missing 1 required positional argument: 'str'. This is because the function expects a string argument because it has a parameter `str` defined in line 35, but no argument is provided when calling the function.
# Default arguments: These are arguments that have a default value specified in the function definition. If no value is provided for these arguments when calling the function, the default value is used.
# def default(name=, age=20):
#     "This function prints a passed string into it"
#     print("Name:", name)  # Print the developer's name
#     print ("Age:", age)  # Print the developer's age
#     return
# default()  # Call the function without providing an argument, so it uses the default value "Developer"
# default(age =35, nane="Lenin")  # Call the function with a specific name, which overrides the default value
# default("Name: Carlos")  # Call the function with another specific name 

# # Keyword arguments: These are arguments that are passed to a function by explicitly specifying the parameter name and its value. This allows you to pass arguments in any order.
# def keyword(str):
#     "This function prints a passed string into it"
#     print(str)  # Print a greeting message with the string
#     return
# # Call the positional function with a keyword argument
# keyword(str="keyword explanation!")  #Directly specify the parameter name `str` and its value "keyword explanation!" when calling the function. This allows you to pass the argument without worrying about its position in the function definition.
# # Example 2
# def devInfo(name, age):
#     "This function prints the name and age of a developer"
#     print(" Name: ", name)  # Print the developer's name and age
#     print(" Age: ", age)  # Print the developer's age
#     return
# # Call the devInfo function with keyword arguments
# devInfo(age=25, name="Lenin")  # Pass the arguments in a different order using keyword arguments. The function will correctly assign the values to the parameters based on their names.

#Python variable scope
# Variable scope refers to the visibility and lifetime of a variable within a program. In Python, variables can have different scopes depending on where they are defined. The two main types of variable scope are:
# 1. Local Scope: Variables defined inside a function have local scope, meaning they are only accessible within that function. They cannot be accessed outside the function.
#Example
def localVar():
    "This function demonstrates local variable scope, it cant be accessed outside this function"
    a=20
    b=30
    print("Local variable a is: ", a)  # Print the local variable a
    print("Local variable b is: ", b)  # Print the local variable b
    return a+b  # Return the sum of a and b
print("Sum of local variables a and b is: ", localVar())  # Call the function and print the result
# print("Local variable a is: ", a)  # This will raise an error: NameError: name 'a' is not defined, because a is defined inside the function and cannot be accessed outside it.


# 2. Global Scope: Variables defined outside any function have global scope, meaning they can be accessed from anywhere in the program, including inside functions.
devName= "Covenant"  # Global variable defined outside any function
grade= 5
def globalVar():
    "This function demonstrates global variable scope, it can be accessed inside this function"
    print("Name: ", devName)  # Print the global variable devName
    print("Grade: ", grade)  # Print the global variable grade

globalVar()  # Call the function to demonstrate global variable access