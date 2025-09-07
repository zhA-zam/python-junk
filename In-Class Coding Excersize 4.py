'''
Mr. Ratburn has given his students a list of words. He has asked them to scan the list in
order and move any word that starts with a vowel to the start of the list. At the end of this
task, all words that start with a vowel would be listed before words that do not start with a
vowel. Mr. Ratburn needs help with the answer key.

Create a program that scans a list of words, does the required task, and prints the modified
list of words.
'''
vowels = ['a', 'e', 'i','o','u']
words = ['castle','apple','markers','pencil','elephant']

# How do I want to access the list?
# 1. You can go over the items in the list without the index
# 2. You can go over the list using the position # (answer is 2nd method)

# Note:
alist = [1,2,3,4]
# add an item at the end of the list
alist.append(5)
print(alist)
# insert a number
alist.insert(2,2.5)  # inserts 2.5 at position 2 of the list
print(alist)
# ridding a number
alist.pop(2)  # removes the number at position 2
print(alist)

# Mr. Ratburn's Problem:
for index in range(len(words)):  # for 5 in range(5) ---> 0,1,2,3,4
    word = words[index]  # subscription: will get me the word at that index
    if word[0] in vowels:
        words.pop(index)
        words.insert(0,word)
print(words)  # Success!

'''
Mr. Ratburn has come up with the following challenging task for his students:
Write all odd numbers between 1 to 100 (both endpoints included) that are divisible by 5 or 7.
Find and write the average of all even numbers between 1 to 100 that are divisible by 5 or 7.

His plan is to nominate students who complete the task correctly for the Annual Math Whiz Award.
Help Mr. Ratburn prepare an answer key by creating a program that does the required task.
'''
# Note that: % checks if there's a remainder
a = 4%2
print(a)
b = 9%2
print(b)

# The problem:
even = []
for number in range (1,101):
    if number % 2 == 0:
        even.append(number)
    else:
        if number % 5 == 0 or number % 7 == 0:
            print(f'{number} is divisble by 5 or 7.')
            
average = sum(even)/len(even)
print(f'{average} is the average of the even numbers')

# Help with v4 of lab2

names = ['Sarah','Bob','Alice','Fred']
grades = [70,85,90,79]
upper = []
lower = []

# Names of students whose grades are above 80
for index in range(len(names)): # length = 3 --> range(3) --> 0, 1, 2
    if grades[index] >= 80:
        print(names[index])

for index in range(len(names)): 
    if grades[index] >= 80:
        upper.append(names[index])
    else:
        lower.append(names[index])
print(' and '.join(upper),"have grades higher than 80")
print(' and '.join(lower),"have grades lower than 80")

# Introduction to while loops
'''
Sookie wants to make trout
'''