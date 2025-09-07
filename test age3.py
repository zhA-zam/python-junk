pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901

chara_name = input("Enter the character's name: ")
chara_age = int(input("Enter the character's age: "))

if chara_age > 0:
    if chara_age < pippin_age:
        print(chara_name,"is",chara_age,"years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
    elif chara_age < frodo_age and chara_age > pippin_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Pippin.") 
        print(chara_name,"is",chara_age,"years old, and they are younger than Arwen, Gollum, Frodo.")    
    elif chara_age > frodo_age and chara_age > pippin_age and chara_age < gollum_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Frodo, Pippin.")
        print(chara_name,"is",chara_age,"years old, and they are younger than Arwen, Gollum.")
    elif chara_age > frodo_age and chara_age > pippin_age and chara_age > gollum_age and chara_age < arwen_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Gollum, Frodo, Pippin.")
        print(chara_name,"is",chara_age,"years old, and they are younger than Arwen.")
    elif chara_age > frodo_age and chara_age > pippin_age and chara_age > gollum_age and chara_age > arwen_age:
        print(chara_name,"is",chara_age,"years old, and they are older than Arwen, Gollum, Frodo, Pippin.")
else:
    print("Invalid age.")