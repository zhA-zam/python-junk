''' Write a Python function called unzip that takes in a dictionary as an argument. 
The function uses the dictionary to create two separate lists. One list contains the 
keys of the dictionary and the other list contains the values of the dictionary. The 
function returns a tuple of two lists. 

For example a call to unzip({'Ten':10,'Twenty':20,'Thirty':30}) returns (['Ten','Twenty','Thirty'],[10,20,30]) 
'''

def unzip(dictionary):
    keys = []
    values = []
    for key in dictionary:
        keys.append(key)
        values.append(dictionary[key])
    return keys, values

def main():
    dictionary = {'Ten':10,'Twenty':20,'Thirty':30}
    unzip_ = unzip(dictionary)
    print(unzip_)
    
main()