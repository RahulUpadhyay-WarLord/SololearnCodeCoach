# Pig Latin +50 XP

##############################
#### Problem Description #####
##############################

# You have two friends who are speaking Pig Latin to each other! Pig Latin is the same words in the same order except that you take the first letter of each word and put it on the end, then you add 'ay' to the end of that. ("road" = "oadray")

# Task
# Your task is to take a sentence in English and turn it into the same sentence in Pig Latin!

# Input Format
# A string of the sentence in English that you need to translate into Pig Latin. (no punctuation or capitalization)

# Output Format
# A string of the same sentence in Pig Latin.

# Sample Input
# "nevermind youve got them"

# Sample Output
# "evermindnay ouveyay otgay hemtay"

##############################
########## Solution ##########
##############################

# Take Sololearn input
startingSting = input()
# Split the string into list on the default delimiter value of any white space
stringSplit = startingSting.split()

# Loop through each item in the list
for i in range(len(stringSplit)):
    # Replace the current item with the pig latin version.
    # stringSplit[i][1:] is 2nd character of string through end
    # stringSplit[i][0:1] is 1st character of string
    # An "ay" is concatinated at the end of the new string
    stringSplit[i] = stringSplit[i][1:] + stringSplit[i][0:1] + "ay"

# Join the new array together with a space in between each
finalString = " ".join(stringSplit)
print(finalString)