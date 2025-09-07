'''
By: Zoha Azam
Date: March 13, 2023
'''

# Excercise 1)
def mylen(some_list):
    if some_list == []:
        return 0
    else:
        return 1 + mylen(some_list[1::2]) + mylen(some_list[2::2])  # CHANGE THIS
        
def main():
    alist=[]
    print(mylen(alist))
main()    

# Excercise 2)
def intDivision(dividend, divisor):
    if dividend < 0 or divisor <= 0:
        raise ValueError("The divisor has to be greater than 0 . ")
    if dividend<divisor:
        return 0
    return 1+intDivision(dividend-divisor,divisor)    

def main():
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m))
main()    

# Excercise 3)
def sumDigits(some_num):
    if len(str(some_num)) == 1:
        return some_num
    else:
        return (some_num % 10 + sumDigits(int(some_num / 10)))
    
def main():
    number = int(input('Enter a number: '))
    print(sumDigits(number))
main()    

# Excercise 4)

    