#Following along with "Automate the boring stuff with python"
#I thought this challenge was really fun.
#I got stuck on where I had to loop at but I figured it out eventually.
import os

os.system('cls') #Clearing terminal.
number = False #Is there a better way?

while number == False: #Loops until user enters a valid int
    try:
        number = int(input('Input a number: ')) 

    except ValueError: #Checks if user input is a valid int
        print('Please enter a number.')


def collatz():
    global number #Uses the global var instead of creating it locally
    while number != 1: #Loop start
        if number % 2 == 0: #Checks if number is even
            number = number // 2
            print(number)
        else: #runs if number is odd
            number = 3 * number + 1
            print(number)

collatz()
