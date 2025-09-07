'''
By: Zoha Azam
Date: October 14, 2023
'''
import random

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    
    filename = 'spells.txt'
    mode = 'r'
    file = open(filename, mode) 
    
    file = open(filename, mode)
    list_of_spells = file.readlines()
    file.close()
    return list_of_spells

def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    list_ = read_spells(spells)
    rand_int = random.randint(0,len(list_)-1)
    random_spell = list_[rand_int]
    random_spell = random_spell.strip()
    random_spell = random_spell.lower()
    return random_spell

FILENAME = 'instructions.txt'

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    mode = 'r'
    file = open(FILENAME, mode)
    
    line1 = file.readline()
    line1 = line1.strip()
    line2 = file.readline()
    line2 = line2.strip()  
    
    border = '#' * len(line2)
    
    print(border)
    print("Harry Potter Typing Trainer")
    print(border)

def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    mode = 'r'
    file = open(FILENAME, mode) 
    
    content = file.read()
    file.close
    print(content)  

def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    
    print(f'Type the following spell: {spell}')
    user_input = input()  
    return user_input

def display_feedback(spell: str, user_input: str):  # MAKE CASE INSENSITIVE!!!
    """
    Displays feedback (correct or incorrect) to the user.
    """
  
    if user_input != spell: 
        print("Incorrect!")
        print(f'The spell was: {spell}')
    if user_input == spell or user_input == spell.upper():
        print("Correct!")
        
def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """

    print("Do you want to practice more? (y/n)")
    play_again = input()
    
    if play_again == 'y' or play_again == 'Y':
        return True
    else:
        return False

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    game_loop = play_again()
    # TODO: Implement the game loop (call play_again function)
    while game_loop:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        display_feedback(spell, user_input)    
    # TODO: Implement scoring system
    # After the game is over, display the final score

main()