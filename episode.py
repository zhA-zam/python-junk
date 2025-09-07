''' 
Converts the original format of an episode title from The Simpsons into
a more readable form for the user and the result displays the reformatted 
version
By: Zoha Azam
Date: September 19, 2023
'''

Episode = input("What is the name of the episode? ")
# Finds the index position of certain parts of the user's input
S_position = Episode.find("S")
E_position = Episode.find("E")
underscore1 = Episode.find("_")
underscore2 = Episode.find("_", underscore1+1)

# Slices certain parts of the user's input that are necessary to maintain for reformatting
season_number = Episode[S_position+1:underscore1]
episode_number = Episode[E_position+1:underscore2]
episode_name = Episode[underscore2+1:]

print("Season",season_number +", Episode",episode_number + ":",episode_name,"(The Simpsons)")  # Displays the reformatted episode title