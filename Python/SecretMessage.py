# Secret Message +50 XP

##############################
#### Problem Description #####
##############################

# You are trying to send a secret message, and you've decided to encode it by replacing every letter in your message with its corresponding letter in a backwards version of the alphabet. 
# What do your messages look like?

# Task: 
# Create a program that replaces each letter in a message with its corresponding letter in a backwards version of the English alphabet.

# Input Format: 
# A string of your message in its normal form.

# Output Format: 
# A string of your message once you have encoded it (all lower case).

# Sample Input: 
# Hello World

# Sample Output: 
# svool dliow

##############################
########## Solution ##########
##############################

# import the copy package to get the deepcopy method.
import copy

# Set starting variables.
# Create a string variable containing the alphabet.
alphabetString = "abcdefghijklmnopqrstuvwxyz"

# Break that string into a list.
alphabetList = list(alphabetString)

# Use the deepcopy method to create an independent list (not a reference to the same list) of the alphabet list, which can then be reversed.
alphabetReverseList = copy.deepcopy(alphabetList)
alphabetReverseList.reverse()

# Take Sololearn inputs
startingString = input()

# Output will be in all lowercase so we can convert the input to lowercase as well.
startingString = startingString.lower()

# Create an empty array to hold the reversed output.
reverseResultList = []

# Loop through each character of the input.
for i in range(len(startingString)):
    # If the character is a space, add a space to reverseResultList.
    if startingString[i] == " ":
        reverseResultList.append(" ")
    # Otherwise, find the current index of the character in the alphabet list. Then use that index value to find the associated character in the reverse list.
    else:
        indexVal = alphabetList.index(startingString[i])
        # Add the reverse alphabet character to reverseResultList.
        reverseResultList.append(alphabetReverseList[indexVal])

# Combine the list of reversed characters into a single string. Since spaces are contained in the list, our join character is blank.
reverseResultString = "".join(reverseResultList)

# Print the results.
print(reverseResultString)