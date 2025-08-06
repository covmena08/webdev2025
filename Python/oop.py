# Classes
# Defining a class
# Syntax:
class ClassName:
    # class body
    pass

#Example:
# class Smartphone:
#     #cunstructor/initialization method (__init__()). It initializes the attributes of the class
#     'This class describes a smartphone with brand and device type'  # Docstring for describing the class
#     def __init__(self, brand, device_type): #The self parameter refers to the instance of the class
#         self.brand = brand
#         self.brand = brand
#         self.device_type = device_type

#     #method of the class
#     def description(self):
#         return f"{self.device_type} of {self.brand} supports Android 15" # f-string for formatting
    
# # Creating an instance of the class
# my_phone = Smartphone("Samsung", "Smartphone")
# print(my_phone.description())

# # print("{self.device_type} of {self.brand} supports Android 15".format(self=my_phone))  # Using format method for string formatting

# str = "Developers"
# print(f"Hello, {str}!")  # Using f-string for string formatting. It formats the string in a more readable way by directly embedding expressions inside curly braces.



#Employee class
class Employee:
    'Base class for all employees'
    empCount = 0
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1  # Increment the employee count each time a new employee is created
    
    def displayCount(self):
        return f"Total Employees: {Employee.empCount} \n"

    def displayEmployee(self):
        return f"Name: {self.name} \nSalary: {self.salary} \n"
    
employeeOne = Employee("Daniel Chisora", 2000)
employeeOne.age = 24 # Add an attribute to Employee class
employeeOne.age = 28 # Modify age
# del employeeOne.age
employeeTwo = Employee("Carol Radul", 2450)
employeeThree = Employee("Fatime Duro", 3400)
print(employeeOne.displayEmployee(), employeeTwo.displayEmployee(), employeeThree.displayEmployee())
getattr(employeeOne, 'age')
print(employeeOne.displayCount())
# Access modifiers: Public, private and protected
# If you want to make an instance variable private, prefix it with double underscore __variableName. This makes it inaccessible from outside the class.
# If you want to make an instance variable private, prefix it with single underscore __variableName.
# Add an instance variable colour, make the device private and brand protected

class Smartphone:
    'This class describes a smartphone with brand and device type'
    def __init__(self, brand, device_type, colour):
        self.__device = device_type  # Private variable
        self._brand = brand  # Protected variable
        self.colour = colour  # Public variable
    
    #method of the class
    def description(self):
        return f"{self.__device} of {self._brand} supports Android 15 and is {self.colour} colour"  # f-string for formatting
#Creating an object for the smartphone class
my_phone = Smartphone("Samsung", "Smartphone", "Black")
print(my_phone.description())

# Name mangling: object._className__privateVariable

# Inheritance OOP (Object-Oriented Programming): Used to inherit to properties and behaviours of one class to another.
# class ParentClass:
#     class body

# Class Childclass(ParentClass, ParentClass1, ParentClass2):
#     child class body

# Single Inheritance: A class inherits from one parent class.
# Parent Class
# class Parent:
#     def parentMethod(self):
#         print("Calling the parent method")

# # Child class
# class Child(Parent):
#     def childMethod(self):
#         print("Calling the child method")

# # Creating an instance of the child class
# child_instance = Child()
# child_instance.parentMethod()  # Calling the parent method from the child class
    
# Implement a solution to give two outputs. The first is the division of two arguements and the second gives the mod value of the operands

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def divide(self):
        return self.a / self.b  # Return the division of a by b

# Modulus class    
class Modulus:
    def __init__(self, c, d):
        self.c = c
        self.d = d
    def mod_divide(self):
        return self.c % self.d  # Return the division of a by b
    

# Child class having multiple inheritance
class Div_Mod(Division, Modulus):
    def __init__(self, e, f):
        self.e = e
        self.f = f
    def div_and_mod(self):
        divVal = Division.divide(self)
        modVal = Modulus.mod_divide(self)
        return (divVal, Div_Mod)
    
value = Div_Mod(10, 3)  # Create an instance of the Div_Mod class with values 10 and 3
print("Division:", value.divide())  # Call the divide method to get the division result
print("Modulus:", value.mod_divide())  # Call the mod_divide method to get the modulus result
print("Division Modulus:", value.div_and_mod())  # Call the div_and_mod method to get both results as a tuple