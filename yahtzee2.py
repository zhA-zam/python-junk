'''
By: Zoha Azam
Date: November 1, 2023
'''
import random

def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    dice = []
    for num in range(1,6):
        rand_int = random.randint(1,6)
        dice.append(rand_int)
    dice = tuple(dice)
    return dice

def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    Example: sum_of_given_number((2,6,2,6,1), 6) = 12
    """
    sum_ = 0
    if number in roll:
        i = 0
        while i < len(roll):
            i = i + 1
            if number is roll[i-1]:
                sum_ = sum_ + 1
    value = number * sum_
    return value

def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    list_of_sums = []
    for i in range(len(roll)+1):
        sum_ = sum_of_given_number(roll,i+1)
        list_of_sums.append(sum_)
    return list_of_sums

def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    for i in range(len(names)):
        print(f'{names[i]}: {upper_section_scores[i]}')
        
def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    # FIX THIS!!!!
    sum_of_all = 0
    for i in range(len(roll)):
        sum_of_all = sum_of_all + roll[i]
    sum_list = fill_upper_section(roll)
    i = 0
    while i < len(roll):
        if roll[i] == 1 and sum_list[0] == roll[i]*number:
            return sum_of_all
        elif roll[i] == 2 and sum_list[1] == roll[i]*number:
            return sum_of_all
        elif roll[i] == 3 and sum_list[2] == roll[i]*number:
            return sum_of_all
        elif roll[i] == 4 and sum_list[3] == roll[i]*number:
            return sum_of_all
        elif roll[i] == 5 and sum_list[4] == roll[i]*number:
            return sum_of_all  
        elif roll[i] == 6 and sum_list[5] == roll[i]*number:
            return sum_of_all 
        else:
            return 0
        i = i + 1

def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    sum_list = fill_upper_section(roll)
    yahtzee = 50
    i = 0
    while i < len(roll):
        if roll[i] == 1 and sum_list[0] == roll[i]*5:
            return yahtzee
        elif roll[i] == 2 and sum_list[1] == roll[i]*5:
            return yahtzee
        elif roll[i] == 3 and sum_list[2] == roll[i]*5:
            return yahtzee
        elif roll[i] == 4 and sum_list[3] == roll[i]*5:
            return yahtzee
        elif roll[i] == 5 and sum_list[4] == roll[i]*5:
            return yahtzee 
        elif roll[i] == 6 and sum_list[5] == roll[i]*5:
            return yahtzee 
        else:
            return 0
        i = i + 1    

def main():
    """
    Main function.
    """
    # TODO: Roll the dice (and print as in demo)
    dice = make_roll()
    print(f'Rolling the dice... {dice}')
    # TODO: Fill the upper section
    sum_list = fill_upper_section(dice)
    print("Upper section:")
    # TODO: Display the upper section
    display_upper_section(sum_list)
    # TODO: Calculate and display "3 of a kind" for the given roll
    print("Lower section:")
    sum_of_all1 = num_of_a_kind(dice, 3)
    print(f'Three of a kind: {sum_of_all1}')
    # TODO: Calculate and display "4 of a kind" for the given roll
    sum_of_all2 = num_of_a_kind(dice, 4)
    print(f'Four of a kind: {sum_of_all2}')
    # TODO: Calculate and display "Yahtzee" for the given roll   
    yahtzee_ = yahtzee(dice)
    print(f'Yahtzee: {yahtzee_}')

if __name__ == "__main__":
    main()