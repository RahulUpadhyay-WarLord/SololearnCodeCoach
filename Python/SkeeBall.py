# Skee-Ball

##############################
#### Problem Description #####
##############################

# You are playing a game at your local arcade, and you receive 1 ticket from the machine for every 12 points that you score. You want to purchase a squirt gun with your tickets. Given your score, and the price of the squirt gun (in tickets) are you able to buy it?

# Task
# Evaluate whether or not you have scored high enough to earn enough tickets to purchase the squirt gun at the arcade.

# Input Format
# The first input is an integer value that represents the points that you scored playing, and the second input is an integer value that represents the cost of the squirt gun (in tickets).

# Output Format
# A string that say 'Buy it!' if you will have enough tickets, or a string that says 'Try again' if you will not.

# Sample Input
# 500
# 40

# Sample Output
# Buy it!

##############################
########## Solution ##########
##############################

# Take Sololearn inputs
points = input()
cost = input()

# Imports come in as strings. Convert them both to integers.
points, cost = [int(points), int(cost)]

# Import the math package to get the floor function
import math

# Divide points by 12 to see how many tickets we earn. Use the floor function to get the actual number of tickets earned.
tickets = math.floor(points/12)
# Using the math package and floor function isn't strictly necessary.
# You could just write: tickets = points/12
# I used the floor function because it isn't possible to earn a partial ticket. You don't get 1/2 ticket for 6 points.

# Simple if statement to determine if we can afford the prize or not. Tickets should be greater than or equal to the cost of the prize.
if tickets >= cost:
    print("Buy it!")
else:
    print("Try again")