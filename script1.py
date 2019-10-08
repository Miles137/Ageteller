#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime
now = datetime.datetime.now()
year = now.year
name = ''
age = 0

def question():
    global name, age
    ans = False
    while ans==False:
        name = input('What is your name? ')
        age = input('How old are you? ')
        ans = True
    return

def message(name, age):
    print('Hi '+ name + '. I hope you are well. You will be 100 years old in the year ' + str(year100) + '.')
    return

question()

year100 = year - int(age) + 100

message(name,age)