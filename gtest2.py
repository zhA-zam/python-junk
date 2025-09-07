import string



text = input("Enter a text to decipher: ")


upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase

        
text_list = []


numbers = []
for number in range(len(upper_case),0,-1):
    numbers.append(str(number))
numbers_string = ''.join(numbers)
print(numbers)
print(numbers_string)
print(upper_case)

for character in text:
    print(list(character))
    if not character.isnumeric():
        special_chara = text.find(character)
        non_letters = text[special_chara]
        text_list.append(non_letters)
    if character in numbers_string:
        print("True")

        


        

    

        
        
print(text_list)
text_string = ''.join(text_list)
a1z26 = text_string.replace('-','')
print(a1z26)
