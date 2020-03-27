# Average Word Length +50 XP

##############################
#### Problem Description #####
##############################

# You are in a college level English class, your professor wants you to write an essay, but you need to find out the average length of all the words you use. It is up to you to figure out how long each word is and to average it out.

# Task:
# Takes in a string, figure out the average length of all the words and return a number representing the average length. Remove all punctuation. Round up to the nearest whole number.

# Input Format:
# A string containing multiple words.

# Output Format:
# A number representing the average length of each word, rounded up to the nearest whole number.

# Sample Input:
# this phrase has multiple words

# Sample Output:
# 6 

##############################
########## Solution ##########
##############################

# Import the math library to get the ceil funcion (rounding up).
# Import the string library filter to be able to fitler out punctuation.
import math
import string

# Take Sololearn input
startingString = input()

# Use string package to filter out punctuation. The third parameter is characters to remove from the string. string.punctuation is a list of common punctuation characters.
startingString = startingString.translate(str.maketrans('', '', string.punctuation))

# Split the string into individual words in a list. (Split with no parameters automatically splits on white space.)
startingList = startingString.split()

# Set variables used to calculate the average word length
stringLength = 0
counter = 0

# Loop through the list of words
for stringItem in startingList:
    # Get the total length of each word in the string
    stringLength = stringLength + len(stringItem)
    # Increment the counter to count the number of words.
    counter = counter + 1

# Divide the total length of the words by the number of words.
# Use the math.ceil function to round the result up to the nearest whole integer.
print(math.ceil(stringLength / counter))