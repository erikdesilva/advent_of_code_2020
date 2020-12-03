import os 

cwd = os.getcwd()
input_txt = os.path.join(cwd, 'input.txt')

with open(input_txt, newline='\n') as input_file:
    lst_data = input_file.readlines()
    dct_passwords = {}
    for i in lst_data:
        i.split(': ')

print(lst_data)