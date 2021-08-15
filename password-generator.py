# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:46:15 2021

@author: Ronak
"""

import string

from random import randint

# Input to determine the password length and whether to include special characters, and if so, how many

# Loop to make sure that a correct length is selected
while True:
    password_len = int(input("How long should the password be? \n"))
    
    if not password_len > 0:
        print('The password length must be greater than zero, please try again')
        continue
    
    else:
        break

# print(f'Your password is {password_len} characters long')

# Loop to make sure Y or N is selected before moving on
while True:
    spec_characters = input("Do you want special characters? (Y/N) \n")
    
    if not spec_characters == "Y" or spec_characters == "N":
        print('Incorrect selection, please try again')
        continue
    
    else:
        break
    
if spec_characters == "Y":
    spec_characters_num = int(input("What is the maximum number of special characters? \n"))
    
if spec_characters == "N":
    spec_characters_num = 0

# Gather a list of lower, upper, and special characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
spec_characters = string.punctuation

# Empty password to begin
password = ""

# Randomly select an integer which will determine if you add a lowercase, uppercase, or special character. Then choose a random character from the string.
# Ensure that the number of special characters does not exceed the inputted amount through a counter.

for i in range(password_len):
    count = 0
    num = randint(0,2)
    
    if num == 0:
        password += str(lower[randint(0,len(lower)-1)])
        
    elif num == 1:
        password += str(upper[randint(0, len(upper)-1)])
        
    elif num == 2:
        if count <= spec_characters_num:
            password += str(spec_characters[randint(0, len(spec_characters)-1)])
            count += 1
            
        elif count == spec_characters_num:
            num2 = randint(0,1)
            if num == 0:
                 password += str(lower[randint(0,len(lower)-1)])
        
            if num == 1:
                password += str(upper[randint(0, len(upper)-1)])
                
print(password)
        
