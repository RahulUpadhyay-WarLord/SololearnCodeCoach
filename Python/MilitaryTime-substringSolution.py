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

# This solution uses substrings

# Take Sololearn input
standardTime = input()

# Search for a colon to identify where the hour starts and ends
# Remember that hours can be 1 or 2 digits (5:00 AM or 11:15 PM) so we can't make assumptions
hourEnd = standardTime.find(':')

# Extract the hour value (everything prior to the colon). Convert it to an int so we can add 12 to it if needed.
hourVal = int(standardTime[0:hourEnd])
# Extract the minute value (the colon and the following two characters). This will always be a consisten length from the colon in this problem.
# The reason I bring in the colon is so we can just paste it back together with the updated hour.
minuteVal = standardTime[hourEnd:hourEnd+3]
# Extract AM/PM value. This will always be the last two characters in this problem.
ampmVal = standardTime[-2:]

# Logic to handle time conversion to military time.
# In each case, the final hour value is converted to a string.
# Any hour less than 10:00 AM will be only a single digit so it will need to be concatenated with a 0.
if ampmVal == "AM" and hourVal < 10:
    hourValStr = '0' + str(hourVal)
# 12:00 AM is represented by 00:00 in military time.
elif ampmVal == "AM" and hourVal == 12:
    hourValStr = '00'
# Anything hour the range of 1:00 PM to 11:00 PM will need 12 added to it
elif ampmVal == "PM" and hourVal < 12:
    hourValStr = str(hourVal + 12)
# Anything not covered above (in this case 10:00 AM, 11:00 AM, and 12:00 PM) will be the same in military time.
else:
    hourValStr = str(hourVal)

# Put the resulting hourParseStr and the value of the minuteParse match object together.
militaryTime = hourValStr + minuteVal

print(militaryTime)