'''
By: Zoha Azam
Date: October 14, 2023
'''
import random
import time

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

FILENAME = 'instructions.txt'  # JUST PUT THIS IN THE FUNCTIONS (AVOID GLOBAL VARIABLES)!!!

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

def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    TTT = len(spell) * 0.3  # TTT = Target Typing Time
    return TTT
    # TODO: Implement this function
    

def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    # TODO: Implement this function

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    # Game loop (call play_again())
    # TODO: Move the score calculation logic from main() to calculate_points()

main()
