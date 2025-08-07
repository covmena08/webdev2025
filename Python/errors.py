#Most common py error: syntax errors
# Missing colons, indentation errors, and unmatched parentheses are common syntax errors in Python.
# 1. Missing colon (:) after a control flow statement (e.g if, for, while, def etc.)

#Example:
# if True
#     print("This will raise a syntax error")  # This line will not execute due to the missing colon

# 2. Indentation error: Python relies on indentation to define blocks of code. If the indentation is inconsistent, it will raise an IndentationError.
# Example:
# def function_Execute():
# print("This will raise an indentation error")  # This line will not execute due to the missing colon

# 3. Missplled keywords: If a keyword is misspelled, Python will raise a SyntaxError.
# Example:
#prnt("This will raise a syntax error")  # This line will not execute due to the misspelled keyword 'print'

# 4. Unmatched parentheses, brackets, or even braces: If you forget to close a parenthesis, Python will raise a SyntaxError.
# Example:
# list= [1, 2, 3, 4, 5  # This line will not execute due to the missing closing bracket
# print(list)  # This line will not execute due to the missing closing bracket


# How to handle errors in Python
# Python provides a way to handle errors using try and except blocks. This allows you to catch exceptions and handle them gracefully without crashing the program.
# Exception handling
# File handling: create, open and close a file

# Syntax:
# open("file_path","mode")
import os
newFile=open("try.py", "w")
newFile.write("We, the developers, just created this file!")
newFile.close()
# Finding out if file was created: 
# print(os.listdir())
# print(os.path.isfile("try.py")) # If terminal says True then our file exists

try:
    fileOpen= open("try.py", "r")
    print(fileOpen.read())
    fileOpen.close() # Always close to not overwehlm memory
except FileNotFoundError:
    print("The file doesn't exist, could you kindly check its details and/or paths?")
finally:
    print("Existing program ... ")

# Logging= logging is the how python stores every user action in messages and it also helps with debugging, keeping records
# (log >> a record)
# Latex is an application that allows researchers to publish their work




