'''
Asks the user for the name and age of a character and displays the given information,
along with whether the character is younger than, older than, or the same age as
Frodo from The Lord of The Rings.

By: Zoha Azam
Date: September 26, 2023
'''

frodo_age = 51  # Contains the value of Frodo's age for later use

# Prompts user input for a character's name and then age
# The age is converted to type int
chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))

# Tests the user's input for the character's age against multiple different
# conditions in succeeding order, based on if the condition is met or not,
# regarding the character's age in relation to Frodo's age
if chara_age > frodo_age:
    print(chara_name,"is",chara_age,"years old, and they are older than Frodo.")
elif chara_age == frodo_age:
    print(chara_name,"is",chara_age,"years old, and they are of the same age as Frodo.")
else:
    print(chara_name,"is",chara_age,"years old, and they are younger than Frodo.")