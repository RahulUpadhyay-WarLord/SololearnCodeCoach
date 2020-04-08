# That's odd... +50 XP

##############################
#### Problem Description #####
##############################

# You want to take a list of numbers and find the sum of all of the even numbers in the list. Ignore any odd numbers.

# Task:
# Find the sum of all even integers in a list of numbers.

# Input Format:
# The first input denotes the length of the list (N). The next N lines contain the list elements as integers.

# Output Format:
# An integer that represents the sum of only the even numbers in the list.

# Sample Input:
# 9
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# Sample Output:
# 20

##############################
########## Solution ##########
##############################

# Take Sololearn input
# The first item will be a number indicating the length of the string.
startingListSize = int(input())

# Define array to store the input numbers
numberList = []

# The remaining items will be a list of numbers.
# Loop for the length of the number entered. Each itteration we will take another input, convert it to an int, and append it to the numberList.
for i in range(startingListSize):
    numberList.append(int(input()))

# Define a variable to store the sum of even numbers
evensum = 0

# Loop through list
for num in numberList:
    # Check if the number is even by using a modulus operation. If so, add it to the sum.
    # A modulus will return the remainder. If there is no remainder, the number is even.
    if num % 2 == 0:
        evensum += num

print(evensum)