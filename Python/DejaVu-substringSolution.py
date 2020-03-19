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

# Take the Sololearn input value
txt = input()

# Value to print at the end of the string.
# If no matches are found, this result will remain unchanged.
result = "Unique"

# Loops through each character in the string.
# Remember to use len()-1 because string characters are zero indexed and len starts at 1.
# Start at the second character (1) because we need to always compare with the previous character
for i in range(1,len(txt)-1):
    # Compare each value in the string with the previous value.
    if txt[i:i+1] == txt[i-1:i]:
        result = "Deja Vu"
        # Break out of the loop. No reason to continue to compare when a match has been found.
        break

print(result)