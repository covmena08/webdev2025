# File handling: refers to the process of performing operations on a file i.e creating, opening, writing, reading, and closing file

# open() syntax
# open(file_name, mode):     # file_name= name of the file you want to open, mode= mode in which the file is to be opened
# Example modes: "r"=read, "w"=write, "a", "x", "b", "t"

# f= open("next.txt")  #open a file in the current dictionary
# f= open("C:/xx/xx/xx") # open in a specified directory

#Creating a text file

# #new_File=open("developers.txt", "x")
# #Checking the file
# print(open("developers.txt", "r").read()==False)
# my_file=open("developers.txt", "w")
# my_file.write("We are the NextStep 2025 Web Development class. \n" )
# my_file.close()

# #Lets read the contents
# my_file=open("developers.txt", "r")
# print(my_file.read())


# # Appending content to a file "a"
# my_file=open("developers.txt", "a")
# my_file.write("We are fulll stack developers, handling both front and backend stuff")
# my_file.close()

# #Lets read the contents
# my_file=open("developers.txt", "r")
# print(my_file.read())


#Cheecking the file properties
# my_file=open("developers.txt", "r")
# print("File Name:", my_file)
# print("Mode:", my_file.mode)
# print("Is the file closed?", my_file.closed)  # Will say False
# #OR
# # print(f"File name: {my_file.name} \n Mode: {my_file.mode}")

# my_file.close()  #Closing the file
# print("After using close() function, is the file closed?", my_file.closed)


# Safe file handling
# Example of try and finally function
# my_file=open("developers.txt", "r")
# try:
#     file_content=my_file.read()
#     print(file_content)
# finally:    #this forces an action, in this case the closing of the file
#     my_file.close()
#print("Is my file closed?", my_file.closed)

#OR 

#Using the with statement instead
# with open("developers.txt", "r") as my_file:
#     file_content=my_file.read()
#     print(file_content) #the file is closed automatically

# print("Is my file closed?", my_file.closed)

# class OurFileManager:
#     def __init__(self, filename, mode):
#         self.filename=filename
#         self.mode=mode
#     def __enter__(self):  #Enters, accesses the file
#         self.file=open(self.filename, self.mode)
#         return self.file
#     def __exit__(self, type, value, traceback): #exiting the file
#         self.file.close()


# #Use our custom context manager using the with statement. Allows you to access the file (write in it?)
# with OurFileManager("developers.txt", "w") as my_file:
#     my_file.write("This file has been safely handled using the custom context manager")


# with OurFileManager("developers.txt", "a") as my_file:
#     my_file.write("We need to append this file as the write mode overwrites all our text")


# Class exercises:
#Group 1
# Write a py program to create a new file called output.txt and write a string of your preference i.e "Hello world I am ..."
# Add another line of code that appends the text to the file that you crated
# Also wriete a few lines of code that display the name of the file, the mode and wether it is closed or not

#Creating the file
new_File2= open("output.txt", "w")
# Checking the file
print(open("output.txt", "r").read()==False)
my_File2=open("output.txt", "w")
new_File2.write("Hello, this is my new file! \n")
new_File2.close()


#Appending the file
my_File2=open("output.txt", "a")
my_File2.write("It outputs data.")
my_File2.close()

# File info
my_File2=open("output.txt", "r")
my_File2.close()
print(f"My new file's name is: {my_File2.name} \n It's mode is: {my_File2.mode} \n My file is closed. {my_File2.closed}")


# 2nd group
# Create a class vehicle and another child class called bus. 
# The bus class will inherit all variables and methods of the vehicle class. Create an object bus that displays the name, max speed, mileage, colour and year of manufacture.


# Homework: Install mysql and a mysql connector