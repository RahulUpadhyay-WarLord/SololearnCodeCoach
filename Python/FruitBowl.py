# Fruit Bowl

##############################
#### Problem Description #####
##############################

# You have a bowl on your counter with an even number of pieces of fruit in it. Half of them are bananas, and the other half are apples. You need 3 apples to make a pie.

# Task
# Your task is to evaluate the total number of pies that you can make with the apples that are in your bowl given to total amount of fruit in the bowl.

# Input Format
# An integer that represents the total amount of fruit in the bowl.

# Output Format
# An integer representing the total number of whole apple pies that you can make.

# Sample Input
# 26

# Sample Output
# 4

##############################
########## Solution ##########
##############################

# Take Sololearn input
import math
fruit = int(input())

# Half of your fruit is apples
apples = fruit/2
# It takes three apples to make a pie
pies = apples/3
# With the floor function, you round down to the nearest integer. i.e. 3.75 rounds to 3. (You can't make a portion of a pie.)
print(math.floor(pies))
