'''
Asks the user for the name and age of a character and displays the given information,
along with whether they are older, or younger, or both, than any of the nine characters
considered the nine companions of the Fellowship of the Ring from The Lord of the Rings.

By: Zoha Azam
Date: September 27, 2023
'''
# Puts the names and ages of nine characters from The Lord of The Rings in parallel
# lists where the indices of the list of names and the list of ages are the same for
# the corresponding names and ages.
names = ["Frodo","Samwise","Gandalf","Legolas","Gimli","Aragorn","Boromir","Merry","Pippin"]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

names_older = []
names_younger = []

# Prompts user input for a character's name and then age
# The age is converted to type int
chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))   

# Stores the names of character who are older or younger than
# the character the user inputs
for index in range(len(names)): 
    if ages[index] > chara_age:
        names_older.append(names[index])
    else:
        names_younger.append(names[index])
        
# Unless the age of the character the user inputs is less than zero, the statement(s)
# of whether said character is older or younger than the nine characters from The Lord
# of The Rings is displayed due to if there are any characters that are older or younger
# than the user's character input.
if chara_age < 0:
        print("Invalid age.")
elif len(names_older) > 0 and len(names_younger) > 0:
        print(f'{chara_name} is {chara_age} years old, and they are older than',", ".join(names_younger))
        print(f'{chara_name} is {chara_age} years old, and they are younger than',", ".join(names_older))
elif len(names_older) == 0 and len(names_younger) > 0:
        print(f'{chara_name} is {chara_age} years old, and they are older than',", ".join(names_younger))
else:
        print(f'{chara_name} is {chara_age} years old, and they are younger than',", ".join(names_older)) 