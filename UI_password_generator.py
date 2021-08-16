# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 00:20:43 2021

@author: Ronak
"""

import string

import random

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Password Generator')
window.iconbitmap('D:/Coding/password-generator/lock.ico')
window.geometry('500x300')

window.configure(bg='dark violet')

def new_pass():
    # Clear entry box
    pass_e.delete(0,END)
    
    # Gather password length and special characters input
    password_len = int(char_e.get())

    spec_characters_num = int(spec_e.get())
    
    # Make sure it is the correct input
    if password_len < 0:
        messagebox.showerror('Error', 'The password length must be greater than 0, please try again')
        
    if spec_characters_num > password_len:
        messagebox.showerror('Error', 'The number of special characters cannot exceed the length of the password')
    
    # Create list of sources to draw from for password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    spec_characters = string.punctuation

    # Empty password to begin
    password = ""

    # Generate password based on input
    for i in range(spec_characters_num):
        password += str(spec_characters[random.randint(0,len(spec_characters)-1)])
        
    remain_char = password_len - spec_characters_num
    
    remain_source = lower + upper
    
    for i in range(remain_char):
        password += str(remain_source[random.randint(0,len(remain_source)-1)])
       
    r_password = ''.join(random.sample(password,len(password)))
    
    # Check if special characters were added correctly, then if special character count and password length are correct, output password
    spec_check = 0
    
    for x in r_password:
        if x in spec_characters:
            spec_check += 1
            
    if spec_check == spec_characters_num and len(r_password) == password_len:
        pass_e.insert(0,r_password)

def copy_to_clip():
    window.clipboard_clear()
    
    window.clipboard_append(pass_e.get())

greet_lf = Label(window, text="Welcome! Please follow the options below", font=('Arial',12),bg='dark violet', fg='gold' )
greet_lf.pack(pady=10)

char_l = Label(window, text = "How long should the password be?", bg='dark violet', fg='gold')
char_l.pack()

char_e = Entry(window, font=("Arial", 10))
char_e.pack()

spec_l = Label(window, text = 'How many special characters do you want to include?', bg='dark violet', fg='gold')
spec_l.pack()

spec_e = Entry(window, font = ('Arial', 10))
spec_e.pack()

pass_e = Entry(window, font = ('Arial', 14),bd=0, bg='dark violet', fg='gold')
pass_e.pack(pady=20, anchor='center')

button_f = Frame(window, bg='dark violet')
button_f.pack()

button_pass = Button(button_f, text = "Generate Random Password", bg='orchid1', command=new_pass)
button_pass.grid(row=0,column=0, padx=10)

button_clip = Button(button_f, text = 'Copy to Clipboard', bg='orchid1', command=copy_to_clip)
button_clip.grid(row=0, column=1, padx=10)


window.mainloop()
