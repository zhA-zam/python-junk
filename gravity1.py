'''
By: Zoha Azam
Date: October 9, 2023
'''
import string

def decrypt_caesar(text: str, shift: int) -> str:
    '''
    Decipher a text (Caesar cipher).
    '''  
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase    
    
    shift = shift % len(upper_case)
    
    text_list = []
    for letter in text:
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

def main() -> None:
    """
    Main program.
    """
    text = input("Enter a text to decipher: ")
    shift = 3    
    caesar_cipher = decrypt_caesar(text, shift)
    print(caesar_cipher)
    
main()