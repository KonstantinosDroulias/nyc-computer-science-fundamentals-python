import FreeSimpleGUI as sg #This is a library I was taught from a course // Still used help form chat gpt
import random as rd
sg.theme('DarkBlue9') # can change themes here https://docs.pysimplegui.com/en/latest/documentation/module/themes/
"""use four lists, lower_case_letters, upper_case_letters, digits, special_characters,
and randomly select a list and then randomly characters from the list."""

#lower_case_letters = ['']

#upper_cae_letters = ['']

#digits = ['']

#special_characters = ['']

#I created the lists and had chatgpt fill them out for me

lower_case_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

upper_case_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', 
    '+', '[', ']', '{', '}', '|', '\\', ';', ':', '\'', '"', ',', 
    '.', '<', '>', '/', '?', '`', '~'
]

combined = lower_case_letters + upper_case_letters + digits + special_characters

def generate_password():
    password =''
    for i in range(0, 10):
        password += rd.choice(combined)
    """I am aware this might have flaws as it might not give something of a whole list ex. might not contain digits but it works for this simple project"""
    return password
    
layout = [
    [sg.Text('Generated Password:', size=(20, 1))],
    [sg.Text('', size=(20, 1), key='password_display')],
    [sg.Button('Generate Password')]
]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Generate Password':
        new_password = generate_password()
        window['password_display'].update(new_password)
window.close()