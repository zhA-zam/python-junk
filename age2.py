'''
Asks the user for the name and age of a character and displays the given information,
along with whether the character is younger or older than either Frodo or Gollum, from
The Lord of the Rings, or both.

By: Zoha Azam
Date: September 26, 2023
'''
# Values for Frodo's and Gollum's ages contained for later use
frodo_age = 51
gollum_age = 589

# Prompts user input for a character's name and then age
# The age is converted to type int
chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))

if chara_age > frodo_age:
    # As long as the character the user inputs the name and age of is older than Frodo,
    # then the character's age will also be tested against conditions of whether they
    # are older or younger than Gollum
    if chara_age < gollum_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Frodo but younger than Gollum.")
    elif chara_age > gollum_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Gollum and Frodo.")
else:
    print(chara_name,"is",chara_age,"years old, and they are younger than Frodo and Gollum.")  # If the user's input for the character's age is less than Frodo's 