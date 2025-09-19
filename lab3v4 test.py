'''
Program Comments

By: Zoha Azam
Date: October 2, 2023
'''
import random

filename = 'klingon-english.txt'
mode = 'r'
file = open(filename, mode)  

klingon_consonants = ['b', 'ch', 'D', 'gh', 'H', 'j', 'l', 'm', 'n', 'p', 'q', 'Q', 'r', 'S', 't', 'v', 'w', 'y', "'"]
    
print("Which consonant do you want to practice with?")
consonant = input("> ")

while consonant not in klingon_consonants:
    print('Please enter a valid Klingon consonant.')
    consonant = input("> ")
    
for line in file:
    line = line.strip() 
    klingon_english = line.split('|')
    translation = ''
    attempts = 0
    max_attempts = 3  
    if klingon_english[0].startswith(consonant):    
        while translation != klingon_english[0] and attempts < max_attempts:
            print(f'How do you translate {klingon_english[1]} to Klingon? You have {max_attempts-attempts} attempts left.')
            translation = input("> ")
            attempts = attempts + 1
            if translation != klingon_english[0]:
                if attempts == 1:
                    first_character = str(klingon_english[0])[0]
                    last_character = str(klingon_english[0])[-1]
                    between_characters = klingon_english[0][1:-1]
                    hidden_characters = '*' * len(between_characters)
                    print("Sorry, you're wrong!")
                    print(f'Hint: {first_character}{hidden_characters}{last_character}')
                elif attempts == 2:
                    random_character = between_characters[random.randint(0,len(between_characters)-1)]
                    random_character_index = between_characters.find(random_character)
                    hidden_characters_list = list(hidden_characters)
                    hidden_characters_list.insert(random_character_index,random_character)
                    hidden_characters_list.pop(random_character_index+1)
                    hidden_characters = ''.join(hidden_characters_list)
                    print("Sorry, you're wrong!") 
                    print(f'Hint: {first_character}{hidden_characters}{last_character}')                   
                else:
                    print("Sorry, you're wrong!")
                    print(f'The correct answer is {klingon_english[0]}.')
            else:
                print("Correct!")
 
file.close() 