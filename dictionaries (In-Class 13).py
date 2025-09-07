# 1) A key must be immutable
# 2) A key must be unique within a dictionary

phone_book = {}
phone_book['Fred'] = 5551234
phone_book['Wilma'] = 5552468
phone_book['Sarah'] = 5553690
phone_book['Barney'] = 5551357
print(phone_book)
print(phone_book['Wilma'])

# The 'get' method

Fred = phone_book.get('Fred')
print(Fred)

'''
grades
'''

grades = {'Fred': 80, 'Sarah': 98, 'Barney': 67, 'Wilma': 55}
print(grades.get('Fredd', 'Not in dictionary'))

print("")
# method 1 - using the items method
for key,value in grades.items(): # grades.items() evaluates to a sequence of key,value pairs
    print(key + ':',value)
print("")
# method 2 - using the keys method
for key in grades.keys(): # grades.keys() evaluates to a sequence of keys
    print(key + ':',grades[key])
print("")
# method 3 - using the values method
for value in grades.values(): # grades.values() evaluates to a sequence of values
    print(value)