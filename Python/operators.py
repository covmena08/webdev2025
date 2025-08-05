# Arithmetic Operators; Addition (+), Subtraction (-), Multiplication (*), Division (/), Modulus (%), Exponentiation (**), Floor Division (//)
a=21
b=10
c=0
c=a + b  # Updating the value of c, so c is no longer 0
# Format method = a method used to arrange the output in a specific format
# Example: Addition operation
# print("a is: {} b is: {} a+b is: {}".format(a,b,c))  # Print the values of a, b, and c in a formatted string
# # Subtraction
# c = a - b  # Update c with the result of subtraction
# print("a is: {} b is: {} a-b is: {}".format(a,b,c))
# # Multiplication
# c = a * b  # Update c with the result of multiplication
# print("a is: {} b is: {} a*b is: {}".format(a, b,c))
# # Division
# c = a / b  # Update c with the result of division
# print("a is: {} b is: {} a/b is: {}".format(a,b,c))
# # Modulus
# c = a % b  # Update c with the result of modulus
# print("a is: {} b is: {} a%b is: {}".format(a,b,c))
# # Exponentiation
# c = a ** b  # Update c with the result of exponentiation
# print("a is: {} b is: {} a**b is: {}".format(a,b,c))
# # Floor Division
# c = a // b  # Update c with the result of floor division
# print("a is: {} b is: {} a//b is: {}".format(a,b,c))


# Comparison Operators; Equal (==), Not Equal (!=), Greater Than (>), Less Than (<), Greater Than or Equal (>=), Less Than or Equal (<=). Comparison operators are used to compare two values and return a boolean result (True or False).
# Examples: Comparison operations
a = 21
b = 10
if (a==b):  # Check if a is equal to b if not, nothing will be printed
    print("a is equal to b")
if (a != b):  # Check if a is not equal to b
    print("a is not equal to b")
if (a > b):  # Check if a is greater than b
    print("a is greater than b")
if (a < b):  # Check if a is less than b
    print("a is less than b")
if (a >= b):  # Check if a is greater than or equal to b
    print("a is greater than or equal to b")
if (a <= b):  # Check if a is less than or equal to b
    print("a is less than or equal to b")

# Assignment Operators; Assign (=), Add and Assign (+=), Subtract and Assign (-=), Multiply and Assign (*=), Divide and Assign (/=), Modulus and Assign (%=), Exponentiation and Assign (**=), Floor Division and Assign (//=), And and Assign (&=), Or and Assign (|=), Xor and Assign (^=), Left Shift and Assign (<<=), Right Shift and Assign (>>=).
# Examples: Assignment operations
a=10
#Add and assign
a += 2  # Add 2 to a=10, so a becomes 12
# Subtract and assign
a -= 3  # Subtract 3 from a=12 because value of a was updated, so a becomes 9
# Multiply and assign
a *= 2  # Multiply a=9 by 2, so a becomes 18
# Divide and assign
# a /= 3  # Divide a=18 by 3, so a becomes 6. Note: Division always results in a float in Python 3, so a becomes 6.0
# Modulus and assign
a %= 4  # Get the remainder of a=6 divided by 4, so a becomes 2
# Exponentiation and assign
a **= 3  # Raise a=2 to the power of 3, so a becomes 8
# Floor division and assign
a //= 2  # Perform floor division of a=8 by 2, so a becomes 4
# And and assign
a &= 1 # Perform bitwise AND of a=4 with 1, so a becomes 0
# Or and assign
a |= 2  # Perform bitwise OR of a=0 with 2, so a becomes 2
# Xor and assign
a ^= 1  # Perform bitwise XOR of a=2 with 1, so a becomes 3
# Left shift and assign
a <<= 1  # Perform left shift of a=3 by 1, so a becomes 6
# Right shift and assign
a >>= 1  # Perform right shift of a=6 by 1, so a becomes 3
# Print the final value of a
print("Final value of a is: {}".format(a))  # Print the final value of a after all operations
# Relationship of assignment & arithmetic operators: assignment operators perform an arithmetic operation and then assign the result back to the variable. For example, `a += 2` is equivalent to `a = a + 2`.
# Relationship of asssignment & bitwise operators: assignment operators can also perform bitwise operations and assign the result back to the variable. For example, `a &= 1` is equivalent to `a = a & 1`, where `&` is the bitwise AND operator.

# Bitwise Operators; Bitwise AND (&), Bitwise OR (|), Bitwise XOR (^), Bitwise NOT (~), Left Shift (<<), Right Shift (>>)/
# Bitwiswe operations are performed on the binary representation of integers. Binary numbers(=base 2) are represented using only two digits: 0 and 1. Bitwise operators manipulate these binary digits at the bit level, that is, they operate on the individual bits of the numbers.
# Decimal numbers(=base 10) is a number system that uses ten digits (0-9) to represent values, while binary numbers use only two digits (0 and 1). For example, the decimal number 5 is represented as 101 in binary, where each digit represents a power of 2.
# Octal numbers(=base 8) use eight digits (0-7) to represent values, while hexadecimal numbers(=base 16) use sixteen digits (0-9 and A-F) to represent values. Example: a decimal number 14 is represented as 16 in octal, E in hexadecimal, and 1110 in binary.

# Examples: Bitwise operations
a=20
b=10
c=bin(a)  # Convert a=20 to binary, c becomes '0b10100'
d=bin(b)  # Convert b=10 to binary, d becomes '0b1010'
print("a: {} b: {} in binary value they are: {} {}".format(a, b, c, d))  # Print the binary representation of a and b

e=0
e=a & b  # Perform bitwise AND operation on a and b, e becomes 0. The AND operation compares each bit of a and b, and sets the corresponding bit in the result to 1 if both bits are 1, otherwise it sets it to 0.
print("the AND result is", bin(e))

e=a | b  # Perform bitwise OR operation on a and b, e becomes 30. The OR operation compares each bit of a and b, and sets the corresponding bit in the result to 1 if at least one of the bits is 1, otherwise it sets it to 0.
print("the OR result is", bin(e))  

e= ~a  # Perform bitwise NOT operation on a, e becomes -21. The NOT operation inverts all bits of a, changing 0s to 1s and 1s to 0s.
print("the NOT result is", bin(e))  # Print the binary representation of the NOT


#0=0000
# 1=0001
# 2=0010
# 3=0011
# 4=0100
# 5=0101
# 6=0110
# 7=0111
# 8=1000
#The rule of the sequence of binary numbers is that each digit represents a power of 2, starting from the rightmost digit which is 2^0, then 2^1, 2^2, and so on.
# Function to convert decimal to binary
# bin(n)
#Example:




