import random

def play():
    user = input("What is your move? ('r' for rock, 'p' for paper, and 's' for scissors)")
    opponent = random.choice(['r', 'p', 's'])

    if user == opponent:
        return 'Your move: ' + printUser(user) + '  My move: ' + printOpponent(opponent) + ' - Its a tie!'
    
    if match(user, opponent):
        return 'Your move: ' + printUser(user) + '  My move: ' + printOpponent(opponent) + ' - You won!'
    
    return 'Your move: ' + printUser(user) + '  My move: ' + printOpponent(opponent) + ' - You lost!'

        
def match(user, opponent):
    if (user == 'r' and opponent == 's') or (user == 's' and opponent == 'p') or (user == 'p' and opponent == 'r'):
        return True

def printUser(user):
    userMove = ''
    if user == 'r':
        userMove = 'rock'
    elif user == 's':
        userMove = 'scissors'
    elif user == 'p':
        userMove = 'paper'
    else:
        userMove = 'Invalid Input'

    return userMove

def printOpponent(opponent):
    opponentMove = ''
    if opponent == 'r':
        opponentMove = 'rock'
    elif opponent == 's':
        opponentMove = 'scissors'
    elif opponent == 'p':
        opponentMove = 'paper'
    else:
        return 'Invalid Input'
    
    return opponentMove


