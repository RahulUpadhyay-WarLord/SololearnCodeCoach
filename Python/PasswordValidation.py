# Password Validation +100 XP

##############################
#### Problem Description #####
##############################

# You're interviewing to join a security team. They want to see you build a password evaluator for your technical interview to validate the input.

# Task: 
# Write a program that takes in a string as input and evaluates it as a valid password. The password is valid if it has at a minimum 2 numbers, 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*'), and a length of at least 7 characters.
# If the password passes the check, output 'Strong', else output 'Weak'.

# Input Format:
# A string representing the password to evaluate.

# Output Format:
# A string that says 'Strong' if the input meets the requirements, or 'Weak', if not.

# Sample Input: 
# Hello@$World19

# Sample Output: 
# Strong

##############################
########## Solution ##########
##############################

# Import the regex package
import re

# Take Sololearn input
password = input()

# Use regex to find all numbers in the string
passwordNumbers = re.findall(r'\d', password)

# Use regex to find all special characters from the problem. Putting them in square brackets eliminates their special functions and treats them as literal.
passwordSpecialCharacters = re.findall(r'[!@#$%&*]', password)

# Determine if the password matches all the requirements
if len(password) > 7 and len(passwordNumbers) >= 2 and len(passwordSpecialCharacters) >= 2:
    print('Strong')
else:
    print('Weak')