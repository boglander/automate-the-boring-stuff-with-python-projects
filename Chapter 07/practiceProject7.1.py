import re

lenght_regex = re.compile(r'.{8,}')     # 8 or more char
upper_regex = re.compile(r'[A-Z]')      # upper letter
lower_regex = re.compile(r'[a-z]')       # lower letter
digit_regex = re.compile(r'[0-9]')       # contains a digit

def password_checker(text):
    if lenght_regex.search(text) is None:
        return False
    if upper_regex.search(text) is None:
        return False
    if lower_regex.search(text) is None:
        return False
    if digit_regex.search(text) is None:
        return False
    else:
        return True

password = input('Enter your password please:' )

if password_checker(password) is True:
    print('Your password is strong')
else:
    print('Your password must be at least 8 characters long and must contain at least an upper letter, a lower letter and a digit')
