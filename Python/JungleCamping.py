# Jungle Camping +10 XP

##############################
#### Problem Description #####
##############################

# You are camping alone out in the jungle and you hear some animals in the dark nearby. Based on the noise they make, determine which animals they are.

# Task:
# You are given the noises made by different animals that you can hear in the dark, evaluate each noise to determine which animal it belongs to. Lions say 'Grr', Tigers say 'Rawr', Snakes say 'Ssss', and Birds say 'Chirp'.

# Input Format:
# A string that represent the noises that you hear with a space between them.

# Output Format:
# A string that includes each animal that you hear with a space after each one. (animals can repeat)

# Sample Input:
# Rawr Chirp Ssss

# Sample Output:
# Tiger Bird Snake

##############################
########## Solution ##########
##############################

# Create a dictionary of animal sounds based on the problem description
animalSoundsDict = {
    "Grr": "Lion",
    "Rawr": "Tiger",
    "Ssss": "Snake",
    "Chirp": "Bird"
}

# Take Sololearn input
animalSounds = input()
# Split the string into list on the default delimiter value of any white space
animalSoundsList = animalSounds.split()

# Create a new list to store the animals heard.
animalsHeardList = []

# Loop through each item in the list
for animalSound in animalSoundsList:
    # Look in the animalSoundsDict to get the current animal sound.
    animalsHeardList.append(animalSoundsDict[animalSound])
    # This could also be done with an If statement (i.e. if animalSound == "Grr": "Lion" ...etc)

# Join the new array together with a space in between each
animalsHeard = " ".join(animalsHeardList)
print(animalsHeard)