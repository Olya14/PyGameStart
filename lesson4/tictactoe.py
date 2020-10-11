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
    Welcome to 'Tic-Tac-Toe'

    Chose your symbol/character
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

#print ('Player goes', choices [0])
#print ('Bot goes', choices [1])

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Player'
    else:
        return 'Bot'


def isWinner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or 
        (board[4] == letter and board[5] == letter and board[6] == letter) or 
        (board[7] == letter and board[8] == letter and board[9] == letter) or 
        (board[1] == letter and board[4] == letter and board[7] == letter) or 
        (board[2] == letter and board[5] == letter and board[8] == letter) or 
        (board[1] == letter and board[5] == letter and board[9] == letter) or 
        (board[3] == letter and board[5] == letter and board[7] == letter) or 
        (board[3] == letter and board[6] == letter and board[9] == letter) 
    )

def makeMove(board, letter, move):
    board[move] = letter



def main():
    while True: 
        theBoard = [' '] * 10
        

        playerLetter, botLetter = printWelcome()
        
        gameIsPlaying = True

        while gameIsPlaying:
            # code for for playing

            print('Do you want to play again? (yes/no)')
            if not input().lower().startwith('y'):
                break


if __name__ == '__main__':
     main()