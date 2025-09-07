'''
By: Zoha Azam
Date: October 30, 2023
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

def display_upper_section(roll: tuple, upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    sum_list = fill_upper_section(roll)
    names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    for i in range(len(names)):
        print(f'{names[i]}: {sum_list[i]}')

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
    display_upper_section(dice, sum_list)

if __name__ == "__main__":
    main()
    
    