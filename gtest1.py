import string



text = input("Enter a text to decipher: ")

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase


    
text_list = []
numbers_list = []  

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
print(text_list)
   
text_string = ''.join(text_list)
a1z26 = text_string.replace('-','')
print(a1z26)