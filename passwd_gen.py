from random import randint
import pyperclip
import time
special_char = ['#', '$', '%', '&', '*', '(', ')', 
                #'+',
                 '-', '!', '%']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
whole_base = special_char + lower_case + upper_case + num

passwd_len = int(input('Input the length of the password, min value is 3 : \n'))
# Ensuring that the password contains one upper case letter, one number and one special character for sure.
passwd = upper_case[randint(0, len(upper_case) - 1)]
passwd = passwd + special_char[randint(0, len(special_char) - 1)]
passwd = passwd + num[randint(0, len(num) - 1)]

# Now fill the remaining positions in the password with random stuff
for i in range(3, passwd_len, 1) :
    passwd = passwd + whole_base[randint(0, len(whole_base) - 1)]

# Print the password
print('Here is your secure password : \n' + passwd)

# Ask whether to copy the password to the clipboard
k = input('Do you want to copy the password to clipboard: Enter Y/N:\n')
if k == 'Y' :
    pyperclip.copy(passwd)
    # For security purposes delete the password from clipboard in 30 seconds.
    print('Password copied to clipboard and stays there only for 30 seconds !!!')
    time.sleep(30)
    pyperclip.copy('')

