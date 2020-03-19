# Halloween Candy

##############################
#### Problem Description #####
##############################

# You go trick or treating with a friend and all but three of the houses that you visit are giving out candy. One house that you visit is giving out toothbrushes and two houses are giving out dollar bills.

# Task
# Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from your bag is a dollar bill?

# Input Format
# An integer (>=3) representing the total number of houses that you visited.

# Output Format
# A percentage value rounded up to the nearest whole number.

# Sample Input
# 4

# Sample Output
# 50

##############################
########## Solution ##########
##############################

import math

# Take Sololearn input
houses = int(input())

# 2 out of the total number of houses will be a dollar bill.
# That result is multiplied by 100 to convert the result (i.e. 0.241) to a percentage (i.e. 24.1%)
# Finally the ceil function is used to round up to the nearest whole number (i.e. 24.1 to 25)
x = math.ceil((2/houses)*100)
print (x)