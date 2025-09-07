'''Problem 1
Carol has joined Xtreme Energy Fitness. In order to maximize muscle gain she needs to consume 2
grams of protein per kg of body weight. Carol knows her weight in pounds.
Write a program that asks Carol for her weight in pounds and then determines and prints the grams
of protein that she should consume per day.

Given 1 kg = 2.20462 pounds
'''
# 1. Prompt Carol to enter her weight in lbs
# 2. Convert lbs into kg
# 3. Compute protein
# 4. Display the information
print("Problem 1")

wght_in_lbs = int(input("Enter weight in pounds: "))
wght_in_kg =  wght_in_lbs/2.20462
protein = round(wght_in_kg*2)
print("The amount of protein that Carol needs to consume per day is: " + str(protein) + " grams")

# Note that all objects in this program are mutable

'''Problem 2
A tray of chicken breasts from Costco weighs 2.32 kg. Carol consumed one-third of the packet.
There are 23 grams of protein in each 6 oz chicken breast. Write a program that determines and
prints how much protein (in grams) Carol consumed.

Given 1 kg = 2.20462 pounds
      1 lb = 16 ounces
'''
# 1. Convert kg into lbs
# 2. Convert lbs into oz
# 3. Comput 1/3 of the above
# 4. Compute protein amount
# 5. Display information
print("Problem 2")

wght_in_kg = 2.32
wght_in_lbs = wght_in_kg*2.20462
wght_in_oz = wght_in_lbs*16

consumed = wght_in_oz/3
# 6 oz --> 23 grams of protein
protein_per_oz = 23/6
total_protein = round(consumed*protein_per_oz)
print("The total protein consumed was: " + str(total_protein) + " grams")

'''Problem 3
Carol wants to store the high protein smoothie in a rectangular container of the following
dimensions:
Length = 21.3cm, Width = 26.7cm, Height = 29.7cm
Carol has prepared 8 litres of smoothie to last her for a week.
Write a program that calculates and prints how many containers Carol would need in order to store
the smoothie.

Given:
Volume of a rectangular container = length x width x height
1 cubic centimeter can hold 0.001 litres
'''
# 1. Find volume of container
# 2. Convert volume to litres
# 3. Divide 8 litres by total volume to find the number of boxes
print("Problem 3")
import math

volume_in_cc = 21.3*26.7*29.7
volume_in_litres = volume_in_cc*0.001
# print(volume_in_litres)
boxes = math.ceil(8/volume_in_litres)
print("Carol needs " + str(boxes) + " container(s)")

'''Problem 4
Carol's trainer has given her a workout routine. The excersises in the routine are listed in a
special format that is hard for Carol to understand. Here is an example--
Bench Press: 5x4, 45 secs
means
Perform 5 sets of Bench Press at 4 reps each. Rest for 45 secs between each set.

Write a program that asks for an excersise code in the above format, translates it into a format
that Carol is able to understand, and prints it.
'''
# 1. Use find method to find the position of the colon, x_symbol, and comma
# 2. Use string slicing to extract the name, sets, reps and rest time
print("Problem 4")

#1:
excersise = input("Enter excersise code > ")
colon_position = excersise.find(":")
x_symbol_position = excersise.find("x")
comma_position = excersise.find(",")

#2:
Name = excersise[0:colon_position]
Sets = excersise[colon_position+1:x_symbol_position]
Reps = excersise[x_symbol_position+1:comma_position]
Rest_Time = excersise[comma_position+1:]

print("Perform" + Sets + " sets of " + Name + " at " + Reps + " reps each. Rest for " + Rest_Time + " between each set.")