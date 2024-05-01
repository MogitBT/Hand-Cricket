import random
import time

def toss(b,c,):
    d = b + c
    if d % 2 == 0:
        e = "even"
    else:
        e = "odd" 

    if e == a:
        print(f'It is {a} you won the toss')
    else:
        print(f'It is {e} Jarvis won the toss')

def bat_or_bowl(b,c):
    d = b + c
    if d % 2 == 0:
        e = "even"
    else:
        e = "odd"
    if e == a:
        return 1
    else:
        return 0

def bat(total_balls):
    total = 0
    n = 1
    out = 0
    while n <= total_balls and out == 0:
        strike1 = int(input("\nyour strike:"))
        jarvis_bowl = random.randint(0,7)
        if strike1 != jarvis_bowl:
            total = total + strike1
            print(f'jarvis={jarvis_bowl}  Total score={total}')
        else:
            print("your wicket gone")
            out = 1
        n = n + 1
    return total

def bowl(total_balls):
    total = 0
    n = 1
    out = 0
    while n <= total_balls and out == 0:
        player_bowl = int(input("\nyour ball:"))
        strike1 = (random.randint(1,6))
        print(f'jarvis: {strike1}')
        if strike1 != player_bowl:
            total = total + strike1
            print(f'you = {player_bowl}  Total score={total}')
        else:
            print("jarvis 0ut")
            out = 1
        n = n + 1
    return total

def bowl1(total_balls):
    total = 0
    n = 1
    out = 0
    while n <= total_balls and out == 0:
        player_bowl = int(input("\nyour ball:"))
        strike1 = (random.randint(1,6))
        print(f'jarvis: {strike1}')
        if strike1 != player_bowl:
            total = total + strike1
            print(f'you = {player_bowl}  Total score={total}')
        else:
            print("jarvis 0ut")
            out = 1
        n = n + 1
    return total


a = input("Odd or Even : ")
b = int(input("enter a number: "))
c = random.randint(1, 7)
time.sleep(1)
print(f'jarvis : {c}')
toss(b,c)

option = bat_or_bowl(b,c)

time.sleep(1)
player_choice = ""
if option == 1:
    player_choice = input("bat or bowl : ")
    player_choice = player_choice.lower()
    if player_choice == "bat":
        print("You choosed to Bat")
    else:
        print("You choosed to Bowl")

jarvis_choice = ""
if option == 0:
    jarvis_choice = "bat"
else:
    jarvis_choice = "bowl"
print(f'jarvis choosed to {jarvis_choice}')

total_overs = int(input("enter total number of overs:"))
total_balls = total_overs * 6

time.sleep(1)
second = 0
score = 0
if player_choice == "bat":
    score = bat(total_balls)
    second = 1
    print(f'your total score = {score}')
elif player_choice == "bowl":
    score = bowl(total_balls)
    second = 2
    print(f'your total score = {score}')
elif jarvis_choice == "bat":
    score = bowl1(total_balls)
    second = 3
    print(f'Jarvis total score = {score}')

time.sleep(1)
score2 = 0
if second == 1:
    print("Ready to bowl")
    score2 = bowl(total_balls)
elif second == 2:
    print("Ready to bat")
    score2 = bat(total_balls)
elif second == 3:
    print("Ready to bat")
    score2 = bat(total_balls)
print(score2)

time.sleep(1)
if score > score2:
    if player_choice == "bat" and jarvis_choice == "bowl":
        run = score - score2
        print(f'congratulations you have won by {run} 🤩')
    else:
        run = score - score2
        player_choice == "bowl" and jarvis_choice == "bat"
        print(f'''Jarvis won by {run} runs 🥳
                better luck next time''')
else:
    if score < score2:
        if player_choice == "bat":
            run = score2 - score
            print( print(f'congratulations you have won by {run1} 🤩'))
        else:
            print('''Jarvis won
               sorry better luck next time''')
