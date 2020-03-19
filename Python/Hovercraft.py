# Hovercraft

##############################
#### Problem Description #####
##############################

# You run a hovercraft factory. Your factory makes ten hovercrafts in a month. Given the number of customers you got that month, did you make a profit? It costs you 2,000,000 to build a hovercraft, and you are selling them for 3,000,000. You also pay 1,000,000 each month for insurance.

# Task:
# Determine whether or not you made a profit based on how many of the ten hovercrafts you were able to sell that month.

# Input Format:
# An integer that represents the sales that you made that month.

# Output Format:
# A string that says 'Profit', 'Loss', or 'Broke Even'.

# Sample Input:
# 5

# Sample Output:
# Loss

##############################
########## Solution ##########
##############################

# Take Sololearn input
sales = int(input())

# Set variables used by the program based on the problem description
# This could be combined into a smaller code set, buy I broke it into multuiple chunks for clarity.
# For example, instead of degining a variable for each portion, I could have just done something like:
# totalCost = (10 * 2000000) + 1000000
hovercrafts = 10
costs = 2000000 * hovercrafts
insurance = 1000000
totalCost = costs + insurance
gross = sales * 3000000

# Compare the totalCost with the gross profit to determine if we made money or not.
if gross > totalCost:
    print("Profit")
elif gross < totalCost:
    print("Loss")
# The else will only capture results not captured above. In this case: equal values.
else:
    print("Broke Even")
