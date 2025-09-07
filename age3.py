'''
Asks the user for the name and age of a character and displays the given information,
along with whether the characters of Pippin, Frodo, Gollum and Arwen--from The Lord of
the Rings--are either younger or older than the character whose name and age the user 
input.

By: Zoha Azam
Date: September 27, 2023
'''
# Values for the ages of Pippin, Frodo, Gollum, and Arwen
# contained for later use
pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901

# Prompts user input for a character's name and then age
# The age is converted to type int
chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))

if chara_age > 0:
    # As long the user's input for the character's age is greater than zero, then the
    # character's age will also be tested against conditions of whether they are only
    # younger than the youngest character, only older than the oldest character, or in
    # between the ages of the other characters.
    if chara_age < pippin_age:
        print(f'{chara_name} is {chara_age} years old, and they are younger than Arwen, Gollum, Frodo, Pippin.')
    elif chara_age < frodo_age and chara_age > pippin_age:
        print(f'{chara_name} is {chara_age} years old, and they are older than Pippin.') 
        print(f'{chara_name} is {chara_age} years old, and they are younger than Arwen, Gollum, Frodo.')    
    elif chara_age > frodo_age and chara_age < gollum_age:
        print(f'{chara_name} is {chara_age} years old, and they are older than Frodo, Pippin.')
        print(f'{chara_name} is {chara_age} years old, and they are younger than Arwen, Gollum.')
    elif chara_age > gollum_age and chara_age < arwen_age:
        print(f'{chara_name} is {chara_age} years old, and they are older than Gollum, Frodo, Pippin.')
        print(f'{chara_name} is {chara_age} years old, and they are younger than Arwen.')
    elif chara_age > arwen_age:
        print(f'{chara_name} is {chara_age} years old, and they are older than Arwen, Gollum, Frodo, Pippin.')
else:
    print("Invalid age.")  # The user's input for the character's age is a negative number