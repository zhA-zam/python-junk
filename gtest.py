import string



text = input("Enter a text to decipher: ")

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase


        
text_list = []

alphabet = []
for letter in upper_case:
    alphabet.append(letter)
    numbers = []
for number in range(1, len(upper_case)+1):
    numbers.append(number)
numbers = ' '.join(numbers)
print(alphabet)
print(numbers)

number_word = text.split(' ')
text_letter = []
for word in number_word:
    number_letter = word.split('-')
    for letter in number_letter:
        if letter.endswith('.'):
            letter = letter.strip('.')
        text_letter.append(letter)

print(text_letter)
special_chara = []

        

    

        
        
print(text_list)
text_string = ''.join(text_list)
a1z26 = text_string.replace('-','')
print(a1z26)




    
        

