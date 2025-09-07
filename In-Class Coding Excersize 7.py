'''
Billy and Nick have been chosen for an internship at Google. Their first 
assignment is to create a signup form that a web ...
'''

# Implement check_user_name - should havve one @ and valid domain
# Type annotation - form of documentation - mandatory
# Implements check_passwords_match
# Implements 4 other functions:
# 1) check_password_len
# 2) check_password_digit
# 3) check_password_capital
# 4) check_password_special


def check_password_special(password:str)->bool:
    for char in password:
        if not char.isalnum():
            return True
    print('Missing special character!')
    return 

def check_password_capital(password:str)->bool:
    for char in password:
        if char.isupper():
            return True
    print('Missing capital letter!')
    return False

def check_password_digit(password:str)->bool:
    for character in password:
        if character.isdigit():
            return True
    return False

def check_password_len(password:str,length:int)->bool:
    if len(password) >= length:
        return True
    return False

def check_passwords_match(password1,password2):
    if password1 == password2:
        return True
    return False
    
def check_user_name(name:str,domains:list)->bool:
    if name.count('@') == 1:
        name_email = name.split("@")
        email_domain = name_email[1]
        if email_domain in domains:
            print("Valid username - proceed to password")
            return True
    print("Invalid username")
    return False

def main()->None:
    username = input("Enter user name: ")
    domain_list = ["ualberta.ca","gmail.com"]
    required_length = 8
    result = check_user_name(username,domain_list)
    if result:
        password = input("Enter password: ")
        password_again = input("Enter password again: ")
        match = check_passwords_match(password,password_again)
        if match:
            has_length = check_password_len(password,required_length)
            has_digit = check_password_digit(password)
            has_capital = check_password_capital(password)
            has_special = check_password_special(password)
            if has_length and has_digit and has_capital and has_special:
                print('Account Registered')            
            
main()

