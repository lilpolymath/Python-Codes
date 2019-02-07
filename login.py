import math
import time
import os

#Welcome Menu
print('Welcome to My Easy Database Maker')
print('What would you like to do')
print('1. Register ')
print('2. Login')
user_input = int(input("Your Choice: "))

#Login Module
if user_input == 2:
    print('')
    print("Login to access the module")
    name = input("Enter your name: ")
    pswd = input("Enter your Password: ")
    print('')

    #Verification Point
    print("Authenticating Username and Password..")
    time.sleep(2)
    print("Cross-Checking Database...",)
    time.sleep(2)
    print("Verifying Login Details...")
    time.sleep(2)
    print("Verification Complete...\n")
    time.sleep(2)
    if name == 'Admin' and pswd == '123456':
        print('Welcome ', name)
        print('Full Content would be available soon')
    else:
        print('Please, login with your correct details')

    #Menu ==> Full Package
quit
