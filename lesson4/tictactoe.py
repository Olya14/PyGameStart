"""
1. input X, O, random?
2. who goes first?
3. save data and update table
4. check win?
5. result
6. play again?
""" 
import random


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O? ').upper()

    if letter == 'X':
        return ['X', 'O'] #[player, bot]
    else:
        return ['O', 'X'] #[player, bot]

def choiceRandom():
    if random.randint(0, 1) == 0:
        return ['X', 'O'] # 'Bot'
    else:
        return ['O', 'X'] # 'Player'

def choiceX():
    return ['X', 'O'] #[player, bot]

def choiceO():
    return ['O', 'X']

#print(inputPlayerLetter()) # check!
def printWelcome():
    menu = """
    Menu:
    1. Choice X
    2. Choice O
    3. Random
    4. Input
    """
    print(menu)
    choice = 0
    while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        choice = int(input('Are you choosing 1 or or O? ')) # str -> int

    if (choice == 1):
        return choiceX() 
    elif (choice == 2):
        return choiceO()
    elif (choice == 3):
        return choiceRandom()
    elif (choice == 4):
        return inputPlayerLetter()
    else:
        return -1 # ERROR

choices = printWelcome()
print ('Player goes', choices [0])
print ('Bot goes', choices [1])