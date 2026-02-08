import math
import re

def is_secure_password(password):

    if len(password) < 8:
        print("Weak password")
    
    elif len(password) >= 8 and len(password) < 12:
        print("Moderate password")
    elif len(password) >= 12 :
        print("Strong password")

def has_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password):
    return bool(re.search(r'[a-z]', password))

def has_digit(password):
    return bool(re.search(r'[0-9]', password))

def has_special_character(password):
    return bool(re.search(r'[@$!%*?&-_+]', password))

def encrypt_password(password):
    entropy = len(password) * math.log2(26 + 26 + 10)
    encrypted = ''.join(reversed(password)) + str(int(entropy))
    return encrypted
def common_passwords_check(password):
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password1", "12345678", "111111", "1234567", "sunshine"]
    return password in common_passwords


print("Please enter your password: ", end="")
password = input()
print("\n")
is_secure_password(password)
encrypted = encrypt_password(password)
print("Encrypted password:", encrypted)
print ("\nPassword analysis:")

if common_passwords_check(password):
    print("- Password is a common password. Consider changing it.") 


if has_uppercase(password):
    print("- Password contains uppercase letters.")
if has_lowercase(password):
    print("- Password contains lowercase letters.")
if has_digit(password):
    print("- Password contains digits.")
if has_special_character(password):
    print("- Password contains special characters.")
