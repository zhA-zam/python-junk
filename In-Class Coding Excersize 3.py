'''Mr. Ratburn is preparing the quarterly report card. You can help Mr. Ratburn 
do the grade assignment.
Write a program that asks for the mark and then assigns the grade based on the 
following table:
[0, 50] grade is F
(50,60] grade is D
(60,70] grade is C
(70,80] grade is B
(80,100] grade is A
A parenthesis ) or ( indicates that the endpoint value is not included. 
A bracket ] or [ indicates that the endpoint value is included.
The program should proceed with grade assignment only if mark is in the valid 
range of [0 - 100] otherwise it should print the message 'Mark is not valid' 
'''
# Want to take the mark and assign the grade

mark = float(input("Enter mark: ")) # float instead of int because grades can have decimals
if mark < 0 or mark > 100: # Header
    print("Invalid Mark") # Suite
else:
    # Proceed with grade assignment if mark is valid
    if mark <= 50:
        grade = "F"
    elif mark <= 60:
        grade = "D"
    elif mark <= 70:
        grade = "C"
    elif mark <= 80:
        grade = "B"
    else:
        grade = "A"
print(grade)
    
'''
Mr. Ratburn wants to keep track of students who participate in math class. 
He recorded their participation using the following letters:
A means student always participated
U means student usually participated
S means student sometimes participated
R means student rarely participated
N means student never participated

As Mr. Ratburn was preparing the quarterly report, he decided to increase their 
quiz mark by 20% if they have A for participation, 15% if they have U for 
participation, 10% if they have S for participation, 5% if they have R for 
participation and by 0% if they have N for participation.

Create a program that takes in the quiz mark and the participation level. 
The program increases the quiz marks based on the participation level and 
prints the updated quiz mark.
If the quiz mark is less than 50 or the participation is N then program 
displays the message 
"Quiz mark remains unchanged". 
'''
quiz_mark = float(input("Enter quiz mark: "))
changed = False
percent = 0
if quiz_mark >= 50:
    p_level = input("Enter participation comment A, U, S, R, N: ")
   
    if p_level == "A":
        percent = 0.20
    elif p_level == "U":
        percent = 0.15
    elif p_level == "S":
        percent = 0.10
    elif p_level == "R":
        percent = 0.05
    else:
        percent = 0

if percent!= 0:
    quiz_mark = quiz_mark+percent*quiz_mark
    changed = True

print("The student's mark is " + str(quiz_mark))
        
                  