# No Numerals +50 XP

##############################
#### Problem Description #####
##############################

# You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead. Can you go in and edit your phrase to write out the name of each number instead of using the numeral?

# Task:
# Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

# Input Format:
# A string of the phrase in its original form (lowercase).

# Output Format:
# A string of the updated phrase that has changed the numerals to words.

# Sample Input:
# i need 2 pumpkins and 3 apples

# Sample Output:
# i need two pumpkins and three apples

##############################
########## Solution ##########
##############################

# Take Sololearn input
startingSting = input()

# Split the string into an array using the default (split on space character)
startingStingSplit = startingSting.split()

# Create a dictionary of numerals to their word counterparts
numberWords = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten"
}

# Set a loop counter
wordCounter = 0

# Loop through the string array
for word in startingStingSplit:
    # Check if the current word is one of the dictionary keys ("1", "2", "3", etc)
    if word in numberWords.keys():
        # If the word is found is found in the dictionary, replace the current word with its dictionary value.
        startingStingSplit[wordCounter] = numberWords[word]
    # Increase the wordCounter by one so that we can replace the correct word positions in the split string array
    wordCounter = wordCounter + 1

# Join the string split on the space character.
print(" ".join(startingStingSplit))