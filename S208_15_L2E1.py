from random import *
'''
Exercise 1: Private Clubhouse
You are task by a private clubhouse to write a simple program to help with their entry management.
If the person is the club member, display "Welcome to SSTea Party!"
Otherwise, ask for the person's age. If user is above 17, display the message "This clubhouse is for members only. Please head to front counter to sign up for membership."
Otherwise, display the message "Sorry, you are underage to enter this clubhouse."
Save your file as class _ index_L2E1.py (e.g. 201_18 _L2Е1.py)
'''

while True:
    YN = input("ARE YOU A MEMBER???? (YES/NO): ")
    if YN == "YES":
        print("Welcome to SSTea Party!")
        break
    elif YN == "NO":
        age = input("HOW OLD ARE YOU?: ")
        while not age.isnumeric():
            age = input("HOW OLD ARE YOU?: ")
        age = int(age)
        if age > 17:
            print("This clubhouse is for members only. Please head to front counter to sign up for membership.")
            break
        else:
            print("Sorry, you are underage to enter this clubhouse.")
            break
    else: 
        pass