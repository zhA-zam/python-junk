print("CMPUT" + str(174))

# can contactenate objects of different types with commas also:
print("CMPUT",174,3.142)
# Note that commas always add a space in a print function
# Use the first one to be in more control of the format of what's being printed

# Multiplication operator * on a string object
print("4"*2)
print("hello " * 3)

# How the addition operator works on a list
alist = [1,2,3]
alist = [1,2,3] + [4,5]
print(alist)

# How the multiplication operator works on a list
blist = [1,2]
blist = blist*2
print(blist)

clist = ["b"] * 4
print(clist)

word = "eat"
puzzle = ["_"] * len(word)
print(puzzle)

#lab1.4 help
astring = "hello,sadaf,ahmed"
comma1 = astring.find(",")
print(comma1)
comma2 = astring.find(",", comma1+1)
print(comma2)

'''
Mr. Ratburn is a teacher at an elementary school. Unfortunately, 
the school heating system is not working properly.

As per school policy, if the outside temperature falls below -5 degrees 
Celsius, Mr. Ratburn needs to make sure that students are wearing their 
jackets before they enter the classroom.

Write a program that asks Mr. Ratburn for the temperature in Celsius and 
then determines and prints if he needs to ask students to wear a jacket.
'''

temperature = int(input("Enter temperature in Celsius: "))
if temperature < -5: #header
    print("Wear a jacket.") #suite
else: 
    print("You're doing great!")

'''
Mr. Ratburn wants to assign seating in his classroom based on the first letter 
of students' names.

Students whose names start with letters A - M are on the left side of the 
classroom.
Students whose names start with letters N - Z are on the right side of the 
classroom.

You can help Mr. Ratburn assign a side to a student. Write a program that asks 
for a name and then determines and prints which side of the classroom the student 
will be seated.
'''
name = input("Enter student's name: ")

if name[0] >= "A" and name[0] <= "M":
    print("Left")
else:
    print("Right")

# THIS IS UNFINISHED I THINK