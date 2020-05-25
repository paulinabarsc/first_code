import pandas as pd
import time

#Intro -> collect email address, return login name.
email_address = input('Enter your email address here: ').split('@')
login_name = email_address[0]

time.sleep(1)

print('Hello, your login name will be: ' + login_name.capitalize())

#Setting out variables for the password check later.
password = 'MyPassword'
guess = ''
guess_limit = 3
guess_attempts = 1
out_of_guesses = False

time.sleep(1)

print('Before opening the file, you will have to enter the correct password. You only have 3 attempts.')

time.sleep(1)

#Password check loop
while guess != password and not(out_of_guesses):
    if guess_attempts <= guess_limit:
        guess = input('Enter your password here: ')
        guess_attempts += 1
        if guess != password:
            print('Incorrect password, try again')
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Too many attempts, access denied.')
else:
    print('Password correct')
    time.sleep(1)
    sheet = pd.read_csv("gift_file.txt")
    print(sheet)