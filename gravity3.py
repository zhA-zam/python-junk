'''
This program attempts to decipher an encrypted code given by the user using
three methods to find out which method works the best to decrypt the given
code.

By: Zoha Azam
Date: October 9, 2023
'''
import string

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase

def decrypt_caesar(text: str, shift: int) -> str:
    '''
    Decipher a text (Caesar cipher).
    '''       
    shift = shift % len(upper_case)
    
    text_list = []
    for letter in text:
        print(list(letter))
        if not letter.isalpha():
            special_chara = text.find(letter)
            non_letters = text[special_chara]
            text_list.append(non_letters)       
        if letter in upper_case: 
            upper_letter = upper_case.find(letter)
            upper = upper_case[upper_letter-shift]
            text_list.append(upper)
        if letter in lower_case:
            lower_letter = lower_case.find(letter)  
            lower = lower_case[lower_letter-shift]
            text_list.append(lower)
    text_string = ''.join(text_list)
    return text_string

def decrypt_atbash(text: str) -> str:
    """
    Decipher a text (Atbash cipher).
    """
    text_list = []
    for letter in text:
        if not letter.isalpha():
            special_chara = text.find(letter)
            non_letters = text[special_chara]
            text_list.append(non_letters)
        if letter in upper_case:                        # finds the position of any upper case letter given in the user's input
            upper_letter = upper_case.find(letter)      # in the string of upper case letters denoted by upper_case. Then uses the range() 
            reverse_list = []                           # function to have a range of numbers starting from 25 and ending in 0. Then using a for 
            reverse_range = range(25,-1,-1)             # loop on that range of numbers to print each number in the range on it's own in the 
            for index in reverse_range:                 # order of the range (i.e printing the numbers from 25 to 0 individually). THEN appending
                reverse_list.append(index)              # each number to the empty list I created above called reverse_list so now I have a list of numbers
            reverse_index = reverse_list[upper_letter]  # starting from 25 and ending in 0. The I use upper_letter which is the identifier I assigned to the 
            reverse = upper_case[reverse_index]         # first task of finding the position of the upper case letter given in the user's input to index
            text_list.append(reverse)                   # reverse_list (i.e if the user's input was 'A' then the position of 'A' in upper_case is 0. So using 
        if letter in lower_case:                        # the number 0 to index reverse_list, the element at position 0 of reverse_list is 25!!) and I assigned
            lower_letter = lower_case.find(letter)      # the identifier reverse_index to this to give me the number I'd need to find the position of the letter
            reverse_list = []                           # that would be in the reversed position of the user's input upper case letter. Then I use reverse_index on
            reverse_range = range(25,-1,-1)             # upper_case to find the letter that's in the reversed position of the input letter in the string identified by  
            for index in reverse_range:                 # upper_case. Then the letter I get by this final indexing I append to my empty list text_list and then, just like
                reverse_list.append(index)              # with the caesar cipher I turn the list into a string by using the .join method and having the userdef function return that.
            reverse_index = reverse_list[lower_letter]  # Same method for lower case letters but obviously using the lower_case identifier for my string of lower case letters.
            reverse = lower_case[reverse_index]
            text_list.append(reverse)        
    text_string = ''.join(text_list)
    return text_string   

def decrypt_a1z26(text: str) -> str:
    """
    Interprets a line of text given by the user that 
    contains numbers and dashes and replaces each 
    number with a letter of the alphabet at the position 
    the number is.
    - text: input function that asks user for encrypted code, type str
    """
    text_list = []     
    for character in text:
        if not character.isalnum():
            special_chara = text.find(character)
            non_numbers = text[special_chara]
            text_list.append(non_numbers)
    number_words = text.strip('.')
    number_words = number_words.split(' ')
    alphabet = upper_case
    reverse_numbers = []
    alphabets = []
    for index in range(1,len(alphabet)+1):
        str_index = str(index)
        reverse_numbers.append(str_index)
        alphabets.append(alphabet[index-1])
    text_numbers = []
    for word in number_words:
        letters = word.split('-')
        for letter in letters:
            text_numbers.append(letter)
    for index in text_numbers:
        if index in reverse_numbers:
            a1z26_letters = alphabets[int(index)-1]
            text_list.append(a1z26_letters)       
    text_string = ''.join(text_list)
    a1z26 = text_string.replace('-','')
    return a1z26

def main() -> None:
    """
    Calls each of the user defined functions
    and executes the program's code.
    """
    text = input("Enter a text to decipher: ")
    print("Let's try all the methods we have!")
    shift = 3    
    caesar_cipher = decrypt_caesar(text, shift)
    atbash_cipher = decrypt_atbash(text)
    a1z26_cipher = decrypt_a1z26(text)
    print(f'Caesar cipher: {caesar_cipher}')
    print(f'Atbash cipher: {atbash_cipher}')
    print(f'A1Z26 cipher: {a1z26_cipher}')

main()  # Runs the program    