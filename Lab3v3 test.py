'''
Program Comments

By: Zoha Azam
Date: October 2, 2023
'''

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
    while klingon_english[0].startswith(consonant):
        while attempts < max_attempts :
            print(f'How do you translate {klingon_english[1]} to Klingon? You have {max_attempts-attempts} attempts left.')
            translation = input("> ")
            attempts = attempts + 1            
            if translation != klingon_english[0]:          
                if attempts == 1 or attempts == 2:
                    first_character = str(klingon_english[0])[0]
                    last_character = str(klingon_english[0])[-1]
                    between_characters = klingon_english[0][1:-1]
                    between_characters = '*' * len(klingon_english[0][1:-1])
                    print("Sorry, you're wrong!")
                    print(f'Hint: {first_character}{between_characters}{last_character}')
                elif attempts == max_attempts:
                    print("Sorry, you're wrong!")
                    print(f'The correct answer is {klingon_english[0]}.')             
        while attempts <= max_attempts:
            print(f'How do you translate {klingon_english[1]} to Klingon? You have {max_attempts-attempts} attempts left.')
            translation = input("> ")
            attempts = attempts + 1            
            if translation == klingon_english[0]:
                print("Correct!")
            
            