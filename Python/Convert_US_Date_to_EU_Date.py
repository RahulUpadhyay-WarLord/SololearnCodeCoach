# Convert US date to EU date +50 XP

##############################
#### Problem Description #####
##############################

# You and your friends are going to Europe! You have made plans to travel around Europe with your friends, but one thing you need to take into account so that everything goes according to play, is that the format of their date is different than from what is used in the United States. Your job is to convert all your dates from MM/DD/YYYY to DD/MM/YYYY.

# Task: 
# Create a function that takes in a string containing a date that is in US format, and return a string of the same date converted to EU.

# Input Format: 
# A string that contains a date formatting 11/19/2019 or November 19, 2019.

# Output Format: 
# A string of the same date but in a different format: 19/11/2019.

# Sample Input: 
# 7/26/2019

# Sample Output: 
# 26/7/2019

##############################
########## Solution ##########
##############################

# Take Sololearn input
USDateStr = input()

# Import the regex package
import re

# Import the datetime package
from datetime import datetime

# Use regex to identify if the first character of the input is a capital letter (first letter of a month)
USDateStrRe = re.match(r'[A-Z]',USDateStr)

# Use dateime.strptime to create a date object based on the result of the regex match.
if (USDateStrRe is None):
    # If there was no result from the Regex search, date is 11/19/2019 format
    USDate = datetime.strptime(USDateStr,'%m/%d/%Y')
else:
    # If there there was a result from the Regex search, date is in November 19, 2019 format
    # %B is the full month name
    USDate = datetime.strptime(USDateStr,'%B %d, %Y')

# Use dateime.strftime to convert the date object into a string of the required formate.
# To remove the leading zeros from the date (as required by the puzzle) on Linux/Android, use a hyphen between the % and the letter code. (This is the solution that will run on Sololearn)
EUDate = datetime.strftime(USDate,'%-d/%-m/%Y')

# To remove the leading zeros from the date (as required by the puzzle) on Windows, use a pound sign between the % and the letter code.
# EUDate = datetime.strftime(USDate,'%#d/%#m/%Y')

print(EUDate)