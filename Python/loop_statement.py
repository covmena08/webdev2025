#Loops allow us to execute a block of code multiple times until a certain condition is met.
# Python For Loop: A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# Syntax: for IterablevariableName in (keyword) sequence:
#    code to be executed for each item in the sequence


# Traverse a tuple that contains integers and is expected to return the total of all numbers in the tuple

tupleNumbers = (34, 44, 54, 64, 74, 84, 94, 86, 89, 87)  # A tuple containing integers
total=0 #intstantiate the value of total to 0
for numTuple in tupleNumbers:  # Loop through each number in the tuple
    total += numTuple  # Add the current number to the total

print("Total of all numbers in the tuple is: ", total)  # Print the total of all numbers in the tuple

# Example: traverse a list containing integers and print only the numbers that are divisible by 2
#numList = [12, 15, 18, 20, 25, 30, 33, 36, 67, 83, 95 ,52, 64, 83 ,74]  # A list containing integers
#for num in numList:  # Loop through each number in the list
#    if numList % 2 == 0:  # Check if the number is divisible by 2
#        print(num)  # Print the number if it is divisible by 2

#For else loop: A for loop can have an else block that executes when the loop completes normally (i.e., not interrupted by a break statement).
#Syntax:
# for IterablevariableName in (keyword) sequence:
#     code to be executed for each item in the sequence
# else:
#     code to be executed after the loop completes normally
# Example: A range with value 6 and the value of each traversal is printed before the iteration stops and the else block is executed
for count in range(6):  # Loop through numbers from 0 to 5
    print("Iteration No. is: {}".format(count))  # Print the current iteration number
else:
    print("The for loop iteration is completed")  # Print a message after the loop completes normally

#While loop: A while loop repeatedly executes a block of code as long as a specified condition is true.
# Syntax: while condition:
#     code to be executed as long as the condition is true

# Example: 
countNumber= 0  # Initialize a counter variable
while countNumber < 6:  # Loop as long as countNumber is less than 6
    countNumber += 1  # Increment the counter by 1
    print("Iteration No. is: {}".format(countNumber))  # Print the current iteration number
print("The while loop iteration is completed")  # Print a message after the loop completes