# Military Time  +50 XP

##############################
#### Problem Description #####
##############################

# You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock. 

# Task: 
# Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

# Input Format:
# A string that includes the time, then a space and the indicator for AM or PM.

# Output Format:
# A string that includes the time in a 24 hour format (XX:XX)

# Sample Input:
# 1:15 PM

# Sample Output:
# 13:15

##############################
########## Solution ##########
##############################

# This solution uses regex

# Import the re package to get regex functions
import re

# Take Sololearn input
standardTime = input()

# Parse the string for the date format. The first number (character type \d) is used with an * metacharacter to get 0 or more instances.
# This is because the first character in a HH:MM is optional. Sometimes the hour is 1 digit and sometimes it is 2. (5:00 PM and 10:00 AM)
# This regex will match: optional number, number, colon, number number
# Note that I'm using the raw string modifier of r in any string with a \ just to ignore any Python specific meanings.
timeParse = re.search(r'\d*\d:\d\d',standardTime)

# This regex uses the square bracket metacharacters to search for either an A or a P followed by an M.
# Strings of AM and PM will both be captured. 
ampmParse = re.search("[AP]M",standardTime)

# Pull the values of the matched strings out of the match objects using the group().
timeVal = timeParse.group()
ampmVal = ampmParse.group()

# Pull just the hour out of the timeVal.
# Using an ^ metacharacter to indicate I'm only looking for numbers that are at the start of the string.
# This means nothing after the first 1 or two numbers will be captured. As soon the : is hit, the search for matched characters will stop.
hourParse = re.search(r'^\d*\d',timeVal)
# Once again, use the group() method to extract the hour value and then pass it directly into to an int function to convert the string to a number.
hourParseInt = int(hourParse.group())

# This regex will grab the : and the two numbers that follow it.
minuteParse = re.search(r':\d\d',timeVal)

# Logic to handle time conversion to military time.
# In each case, the final hour value is converted to a string.
# 12:00 AM is represented by 00:00 in military time.
if hourParseInt == 12 and ampmVal == "AM":
    hourParseStr = '00'
# 12:00 PM, 11:00 AM, and 10:00 AM will all be the same in military time.
elif (hourParseInt == 12 and ampmVal == "PM") or ((hourParseInt == 11 or hourParseInt == 10) and ampmVal == "AM"):
    hourParseStr = str(hourParseInt)
# Any hour less than 10:00 AM will be only a single digit so it will need to be concatenated with a 0
elif hourParseInt < 10 and ampmVal == "AM":
    hourParseStr = '0' + str(hourParseInt)
# The else will capture anything else (which in this case is 1:00 PM to 11:00 PM) and add 12 to it.
else:
    hourParseStr = str(hourParseInt + 12)

# Put the resulting hourParseStr and the value of the minuteParse match object together.
militaryTime = hourParseStr + minuteParse.group()

# Print the final result
print(militaryTime)