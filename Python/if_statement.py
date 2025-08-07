#Syntax:
# if expression:
    # code to be executed if the expression is true

#Example: A customer recieves a 10% discount if their purchase is above 10000ft else no discount
discount = 0  # Initialize discount to 0
#amount = int(input("Enter the amount: "))  # Get the amount from the user
# Checking if amount is greater than or equal to 10000ft
# if amount >= 10000:
#     discount = 0.1 * amount  # Calculate 10% discount
#     amount= amount-discount
#     print("You need tp pay{}ft, you got a {}ft discount. Thx for shopping with us!!! ", format(amount, discount))  # Print the discount amount


#Using if else statement
#Syntax:
# if bool_expression:
#     # code to be executed if the expression is true
# else:
#     # code to be executed if the expression is false
#Example: If the voter is above 18, they can vote, otherwise they cannot vote
#age = int(input("Enter your age: "))  # Get the age from the user
# if age >= 18:
#     print("You are eligible to vote!")  # Print if the voter is eligible to vote
# else:
#     print("You are not eligible to vote!")  # Print if the voter is not eligible to vote



#Using if elif else statement
#nSyntax:
# if bool_expression1:
#     # code to be executed if the first expression is true
# elif bool_expression2:
#     # code to be executed if the second expression is true
# else:
#     # code to be executed if both expressions are false


#Example: Implement a program that offers a discounts to customers based on their purchase amount
# 20% discount for amounts exceeding 10000ft
# 10% discount for amounts between 5000 < 10000ft
# 5% discount for amounts between 1000 < 5000ft
# No discount discount for amounts under 1000ft

# amount =float(input("Enter the amount: "))
# discount=0
# print("Amount: ", amount)
# if amount >= 10000:
#     discount = 0.2 * amount
# elif amount >= 5000:
#     discount = 0.1 * amount
# elif amount >= 1000:
#     discount = 0.05 * amount
# else:
#    discount = 0

# payableAmount= amount-discount
# print("Payable amount: ", payableAmount, "Subtracted discount: ", discount)