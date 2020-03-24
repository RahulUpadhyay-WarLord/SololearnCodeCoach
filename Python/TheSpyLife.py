# The Spy Life +50 XP

##############################
#### Problem Description #####
##############################

# You are a secret agent, and you receive an encrypted message that needs to be decoded. The code that is being used flips the message backwards and inserts non-alphabetic characters in the message to make it hard to decipher.

# Task:
# Create a program that will take the encoded message, flip it around, remove any characters that are not a letter or a space, and output the hidden message.

# Input Format: 
# A string of characters that represent the encoded message.

# Output Format:
# A string of character that represent the intended secret message.

# Sample Input:
# d89%l++5r19o7W *o=l645le9H

# Sample Output:
# Hello World

##############################
########## Solution ##########
##############################

# Import the regex package (re)
import re

# Take Sololearn inputs
startingString = input()

# Do a regex search on the input. Looking for any letter (lower or upper case) or space.
stringMatch = re.findall(r'([a-zA-Z\s])', startingString)

# findall returns a list. Since spaces are returned by the regex search, we can join them with an empty string as delimiter.
stringJoin = "".join(stringMatch)

# The result will be backwards so we need to reverse the string. We can do a full substring with the step at -1 to go through the string backwards.
print(stringJoin[::-1])