import random

def verifyNumber(guessNumber,correctNumber):
    if(guessNumber>correctNumber):
        print('Too high!')
    else:
        print('Too low!!')

def executeProgram():
    while exitInput != 'q':

    print('Hello, please input your name:')
    playerName = input()

    print('Hi, '+playerName+' number is generate. Please guess~')
    correctNumber = random.randint(0,100)
    guessNumber = 0
    while guessNumber != correctNumber:
        guessNumber = int(input())
        verifyNumber(guessNumber, correctNumber)

    print('Correct! Do you want to play again? Leave please input q:')
    exitInput = input()

exitInput = ''

try:
    executeProgram()
except ValueError:
    print('Unknow input! Program stop.')