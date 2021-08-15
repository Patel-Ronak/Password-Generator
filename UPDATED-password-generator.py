# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 00:20:43 2021

@author: Ronak
"""


import string

import random

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
    while True:
        spec_characters_num = int(input("How many special characters would you like to include? \n"))
    
        if not spec_characters_num <= password_len:
            print('The number of special characters must be less than the length of the password, please try again')
            continue
    
        else:
            break
    
if spec_characters == "N":
    spec_characters_num = 0
    
# Gather a list of lower, upper, and special characters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
spec_characters = string.punctuation

# Empty password to begin
password = ""

for i in range(spec_characters_num):
    password += str(spec_characters[random.randint(0,len(spec_characters)-1)])
    
remain_char = password_len - spec_characters_num

remain_source = lower + upper

for i in range(remain_char):
    password += str(remain_source[random.randint(0,len(remain_source)-1)])
   
r_password = ''.join(random.sample(password,len(password)))

spec_check = 0

for x in r_password:
    if x in spec_characters:
        spec_check += 1
        
if spec_check == spec_characters_num:
    print(f'Your unshuffled password is {password}. Your randomly generated password with {spec_characters_num} special characters is {r_password}')