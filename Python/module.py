import math
import random
print("Square root of 100 is: ", math.sqrt(100))  # Example usage of the math module
start=10
end=40
print("The random number generated between 10 and 40 is: ", random.randrange(start, end))  # Example usage of the random module

def sayHi(name):
    print("Hi {}!!! How are you?".format(name))  # Print a greeting message with the name

def sum(x, y):
    return x + y  # Return the sum of x and y
def difference(x, y):
    return x - y  # Return the difference of x and y
def product(x, y):
    return x * y  # Return the product of x and y
def avarage(x, y):
    return (x + y) / 2  # Return the average of x and y
def exp(x, y):
    return x**y  # Return x raised to the power of y