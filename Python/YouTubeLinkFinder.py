# YouTube Link Finder +50 XP

##############################
#### Problem Description #####
##############################

# You and your friends like to share YouTube links all throughout the day. You want to keep track of all the videos you watch in your own personal notepad, but you find that keeping the entire link is unnecessary. 
# Keep the video ID (the combination of letters and numbers at the end of the link) in your notepad to slim down the URL.

# Task: 
# Create a program that parses through a link, extracts and outputs the YouTube video ID.

# Input Format: 
# A string containing the URL to a YouTube video. The format of the string can be in "https://www.youtube.com/watch?v=kbxkq_w51PM" or the shortened "https://youtu.be/KMBBjzp5hdc" format.

# Output Format: 
# A string containing the extracted YouTube video id.

# Sample Input: 
# https://www.youtube.com/watch?v=RRW2aUSw5vU

# Sample Output: 
# RWW2aUSwvU

##############################
########## Solution ##########
##############################

# Take Sololearn input
link = input()

# Find the start location of the video id based on the two different link formats. Find a section of the link that identifies the format, and then add the appropriate number of characters to the start of the video id.
if link.find('.be/') > -1:
    linkStart = link.find('.be/') + 4
else:
    linkStart = link.find('?v=') + 3

# print the link by substringing from the start of the link through the end of the string. This works by not including a specified number of characters so the substring goes through the end.  
print(link[linkStart:])