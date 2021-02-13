import random
from cric_intro import *
import time

#this function is used to calculate the player score

def player(player_name):
    score=0
    wickets=0
    for i in range(1,6):
        print('Over:',i,'Runs:',end='')          #5 over match
        for i in range(1,7):
            k=random.choice([0,1,2,3,4,6,'W'])     #runs per over
            print(k,'|',end='')
            if k=='W':
                wickets=wickets+1
            else:
                score=score+k
        print()
    print(player_name,'total score:',score,'/',wickets,'\n')
    return score
    
#cmputer() is used calculate the computer score

def computer():
    score=0
    wickets=0
    for i in range(1,6):
        print('Over:',i,'Runs:',end='')
        for i in range(1,7):
            k=random.choice([0,1,2,3,4,6,'W'])
            print(k,'|',end='')
            if k=='W':
                wickets=wickets+1
            else:
                score=score+k
        print()
    print('Computer total score:',score,'/',wickets,'\n')
    return score

#the one with more score is the winner

def winner(ps,cs,name):
    if ps>cs:
        print('\n  ',u"\U0001F3C6",'   ')
        print(name,'won')
    elif ps<cs:
        print('\n  ',u"\U0001F3C6",'   ')
        print('  Computer won')
    else:
        print('Draw')

print(intro)
while True:
    response=input('So, Are you ready to get started(yes/no)?').lower()
    if response.startswith('y'):
        name=input('Enter player name:')

        while True:
            coin_toss=input('Heads/Tails:').lower()
            if 'heads'==coin_toss or 'tails'==coin_toss:
                break
            else:
                continue

        toss=random.choice(['heads','tails'])

        #if the user wins the toss
        if coin_toss==toss:
            print(name,'won the toss')
            choice=input('Bat or Field?').lower()
            print('Match will start in few seconds....')
            time.sleep(5)
            if choice=='bat':
                print(name,'chooses to bat first')
                time.sleep(1.5)
                player_score=player(name)
                print('Second Innings commencing soon \n')
                time.sleep(17)
                computer_score=computer()
            else:
                print(name,'chooses to field first')
                time.sleep(1.5)
                computer_score=computer()
                print('Second Innings commencing soon \n')
                time.sleep(10)
                player_score=player(name)
        else:
            print('Computer won the toss')
            print('Match will start in few seconds....')
            time.sleep(5)
            choice=random.choice(['bat','field'])
            if choice=='bat':
                print('Computer chooses to bat first')
                time.sleep(1.5)
                computer_score=computer()
                print('Second Innings commencing soon \n')
                time.sleep(17)
                player_score=player(name)
            else:
                print('Computer chooses to field first \n')
                time.sleep(1.5)
                player_score=player(name)
                print('Second Innings commencing soon \n')
                time.sleep(10)
                computer_score=computer()

        winner(player_score,computer_score,name)

    else:
        print(ending)
        break