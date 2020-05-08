# Security +100 XP

##############################
#### Problem Description #####
##############################

# You are in charge of security at a casino, and there is a thief who is trying to steal the casino's money!  Look over the security diagrams to make sure that you always have a guard between the thief and the money!
# There is one money location, one thief, and any number of guards on each floor of the casino.

# Task:
# Evaluate a given floor of the casino to determine if there is a guard between the money and the thief, if there is not, you will sound an alarm.

# Input Format:
# A string of characters that includes $ (money), T (thief), and G (guard), that represents the layout of the casino floor.
# Space on the casino floor that is not occupied by either money, the thief, or a guard is represented by the character x.

# Output Format:
# A string that says 'ALARM' if the money is in danger or 'quiet' if the money is safe.

# Sample Input:
# xxxxxGxx$xxxT

# Sample Output:
# ALARM

##############################
########## Solution ##########
##############################

# Take Sololearn inputs.
casino = input()

# Create an array to store guard locations.
guardsLocations = []

# Loop through the casino string to identify the location of the thief, money, and guard(s).
for casinoChar in range(0, len(casino)):
    if casino[casinoChar] == 'x':
        next
    elif casino[casinoChar] == '$':
        moneyLocation = casinoChar
    elif casino[casinoChar] == 'T':
        thiefLocation = casinoChar
    else:
        # Anything else will be a guard.
        guardsLocations.append(casinoChar)

# Set an alarm starting value
alarm = True

# Loop through the guards to identify if any of them are between the thief and money.
for guard in guardsLocations:
    if (moneyLocation < guard < thiefLocation) or (moneyLocation > guard > thiefLocation):
        # If the guard is in between the thief and money, set the alarm to false.
        alarm = False
        break

# If a guard is found between the thief and the money, the alarm will be quiet. If it is still True, the Alarm will sound.
if alarm:
    print("ALARM")
else:
    print("quiet")