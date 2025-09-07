'''
Program Comments
'''

names = ["Frodo","Samwise","Gandalf","Legolas","Gimli","Aragorn","Boromir","Merry","Pippin"]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]
names_older = []
names_younger = []

chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))   

for index in range(len(names)): 
    if ages[index] > chara_age:
        names_older.append(names[index])
    else:
        names_younger.append(names[index])
        

if chara_age < 0:
        print("Invalid age.")
elif len(names_older) > 0 and len(names_younger) > 0:
        print(f'{chara_name} is {chara_age} years old, and they are older than',", ".join(names_younger))
        print(f'{chara_name} is {chara_age} years old, and they are younger than',", ".join(names_older))
elif len(names_older) == 0 and len(names_younger) > 0:
        print(f'{chara_name} is {chara_age} years old, and they are older than',", ".join(names_younger))
else:
        print(f'{chara_name} is {chara_age} years old, and they are younger than',", ".join(names_older))