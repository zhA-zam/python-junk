'''
Decrypts then displays a message encoded by a Casear cipher in a file

By: Zoha Azam
Date: January 21, 2024
'''
import string

def getInputFile():
    '''
    Prompts the user for a file name, checks if the file type is acceptable.
    Accepts the file if it is a '.txt' type, otherwise continues to prompt user
    '''
    text_file = input("Enter file name: ")
    while text_file[-4:] != '.txt':
        print("Error! File type incorrect.")
        text_file = input("Enter file name: ")
        
    return text_file

def decrypt(filename):
    '''
    Deciphers the encrypted message of the file given by the user 
    - filename: name of file given by user
    '''
    file = open(filename, 'r')
    
    file_contents = []
    for line in file:
        line = line.strip()
        file_contents.append(line)
        
    cipher_key = int(file_contents[0])
    message = file_contents[1]

    cipher_key = cipher_key % 26
    
    letters = ''
    
    # Decrypts the message in the file
    for word in file_contents[1:]:
        for char in word:
            if char.isupper():
                letters = letters + chr((ord(char) - cipher_key - 64) % 26 + 64)
            elif char.islower():
                letters = letters + chr((ord(char) - cipher_key - 96) % 26 + 96)
            else:
                letters = letters + ' '
    
    letters = letters.lower()
    return letters 

def main():
    '''
    Main program code
    '''
    filename = getInputFile()
    decrypted_cipher = decrypt(filename)
    print(decrypted_cipher)

main()