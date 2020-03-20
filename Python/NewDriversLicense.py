# New Driver's License

##############################
#### Problem Description #####
##############################

# You have to get a new driver's license and you show up at the office at the same time as 4 other people. The office says that they will see everyone in alphabetical order and it takes 20 minutes for them to process each new license. All of the agents are available now, and they can each see one customer at a time. How long will it take for you to walk out of the office with your new license?

# Task
# Given everyone's name that showed up at the same time, determine how long it will take to get your new license.

# Input Format
# Your input will be a string of your name, then an integer of the number of available agents, and lastly a string of the other four names separated by spaces.

# Output Format
# You will output an integer of the number of minutes that it will take to get your license.

# Sample Input
# 'Eric'
# 2
# 'Adam Caroline Rebecca Frank'

# Sample Output
# 40

# Explanation
# It will take 40 minutes to get your license because you are in the second group of two to be seen by one of the two available agents.

##############################
########## Solution ##########
##############################

# Using the math package to get the floor function
import math

# Take Sololearn inputs
yourName = input()
numberOfAgents = int(input()) # Take number of agents and convert it to an int
otherNames = input()
otherNamesSplit = otherNames.split() # Split the space delimited list of names. (If split doesn't have a character, it divides into a list based on any whitespace.)

# Add your name to the list of names
otherNamesSplit.append(yourName)

# Sort the list of names into alphabetical order
otherNamesSplit.sort()

# Loop through the list if ordered names
for i in range(0,len(otherNamesSplit)):
    # See if the current name from the List matches the name entered into the YourName variable
    if otherNamesSplit[i] == yourName:
        # If it is, divide the current number list item by the number of agents to determine what group they are starting in.
        # Use floor function to round it down to the nearest starting group.
        group = math.floor(i/numberOfAgents) # When your appointment starts

# The problem wants to know what time you will leave the office so we'll add one to the value so it will be multiplied by 20.
group += 1

# Print the final group time ending time multiplied by 20.
print(group*20)