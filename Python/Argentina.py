# Argentina

##############################
#### Problem Description #####
##############################

# You are in a hat store in Argentina! The prices are listed in US Dollars and Argentinian Pesos. You have both, but you want to make sure you pay the lower price! Do you pay in Dollars or Pesos? The exchange rate is 2 cents for every Peso.

# Task
# Create a program that takes two prices and tells you which one is lower after conversion.

# Input Format
# Two integer values, the first one is the price in Pesos and the second one is the price in Dollars.

# Output Format
# A string that says which currency you should make the purchase in ('Dollars' or 'Pesos').

# Sample Input
# 4000
# 100

# Sample Output
# Pesos

##############################
########## Solution ##########
##############################

# Take Sololearn inputs
pesos = input()
dollars = input()

# Convert both inputs to ints and reassign them to the starting variables.
pesos, dollars  = [int(pesos), int(dollars )]

# Convert pesos using the exchange rate from the problem.
pesosConverted = pesos * 0.02

# Simple if statement to determine which has the cheaper purchase option and print the required result.
if pesosConverted < dollars:
    print("Pesos")
else:
    print("Dollars")