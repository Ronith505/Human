print("Please enter your name")
name = input()
print("hello ",name)
print("tell me what you like")
me = input()
print("okay so you like",me)
print("why do you like it")
opinion = input()
print("so you like because",opinion)
print("lets play a game") 
computer_number = 82
prompt = 'What is your guess of your number '
while True:
    players_guess = input(prompt)
    if computer_number == int(players_guess):
        print ('Correct')
        break
    elif computer_number > int (players_guess):
        print('to low')
    else:
        print('too high')
print("good job")
print("so lets play a number game")
from random import seed
from random import randint
seed(1)
oper = input("What operation game do you want play? ")
num1 = randint(1, 10)
num2 = randint(1, 10) 
num1 = int(num1)
num2 = int(num2)
your_answer  = input(f'What is {num1} {oper} {num2} = ?') 

if oper == "+":
        res = num1 + num2
elif oper == "-":
        res = num1 - num2
elif oper == "*":
        res = num1 * num2
elif oper == "/":
        res = num1 / num2

if int(your_answer) == res:
        print(f"\nCongragulation...")
else:
        print(f'\nCorrect answer is {num1} {oper} {num2} = {res}') 
print("Nice Job")
print("so lets play a game")
print("go to typing.com and type on see how fast you are at typing when your done put it here")
answer = input()
print("So your speed at typing is",answer)
print("So who's your dad")
dad = input()
print("So your dad name is",dad)
print("Your Mom")
mom = input()
print("your mom's name is",mom)
print("Your brother or sister")
bro = input()
print("your brother or sisters name is",bro)
print("So now I know your family")
print("now I will upload it to the internet")
print("JK But is is getting late the time is")
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print("when do you sleep")
sleep = input()
print("oh so your bedtime is",sleep)
print("great i can't be up that late")
print("Let's play a number guess game 1-100,00")
computer_number = 100
prompt = 'What is your guess of your number '
while True:
    players_guess = input(prompt)
    if computer_number == int(players_guess):
        print ('Correct')
        break
    elif computer_number > int (players_guess):
        print('to low')
    else:
        print('too high')
print("good job")
print("so lets play a number game")
from random import seed
from random import randint
seed(1)
print("oh god The weather is")
from pprint import pprint
import requests
r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=21704,us&appid=1c43a9e69ac0648181e256238719f140')
pprint(r.json())
print("Do you want to add something with me you can do it try it")
yourname = input("Please enter your name: ")
number1 = input("Please enter number1: ")
number2 = input("Please enter number2: ")
addnumber = int(number1) * int(number2)
print (f'{yourname} addition of 2 numbers : {addnumber}')
print("okay it is getting late go to go see ya")
print("the next day")

