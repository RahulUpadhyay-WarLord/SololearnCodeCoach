# Deja Vu

##############################
#### Problem Description #####
##############################

# You aren't paying attention and you accidentally type a bunch of random letters on your keyboard. You want to know if you ever typed the same letter twice, or if they are all unique letters.

# Task:
# If you are given a string of random letters, your task is to evaluate whether any letter is repeated in the string or if you only hit unique keys while you typing.

# Input Format:
# A string of random letter characters (no numbers or other buttons were pressed).

# Output Format:
# A string that says 'Deja Vu' if any letter is repeated in the input string, or a string that says 'Unique' if there are no repeats.

# Sample Input:
# aaaaaaaghhhhjkll

# Sample Output:
# Deja Vu

##############################
########## Solution ##########
##############################

# Import the regex package (re)
import re

# Take the Sololearn input value
txt = input()

# Do a regex search on the input.
matchCheck = re.search(r'([a-z])\1', txt)
# regex pattern:
# r - convert the input to a Raw String so that the way Python treats \ is ignored
# () - Create a matched group
# [a-z] - match any lowercase character (range of a to z).
# \1 match exactly what was in the first group created (there is only one group)
# ([a-z])\1 - find any single lowercase character: [a-z], group it: (), and then look to see if the next character is an exact match: \1

# If no character match is found, matchCheck returns none - which is a falsy value. Any match found will be treated as a truthy value.
# This allows for a pretty easy if statement.
if (matchCheck):
    print("Deja Vu")
else:
    print("Unique")
