'''
Ask the user for a phrase and displays it's repetition as many times
as the user wants
By: Zoha Azam
Date: September 18, 2023
'''

# Prompts user input on writing a phrase
Phrase = input("What is the phrase? ")
repeat_times = int(input("How many times do you want to write it? "))

print((Phrase+" ")*repeat_times)  # Repeats given phrase by given number of times