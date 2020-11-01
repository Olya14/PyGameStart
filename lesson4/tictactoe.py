"""
1. input X, O, random?
2. who goes first?
3. save data and update table
4. check win?
5. result
6. play again?
 _ _ _
| | | |
 - - -
| | | |
 - - -
| | | |
"""
import random 


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Are you choosing X or O? ').upper()

    if letter == 'X':
        return ['X', 'O'] # [player, bot]
    else:
        return ['O', 'X'] # player, bot

#print(inputPlayerLetter()) # check!

def choiceRandom():
    if random.randint(0, 1) == 0:
        return ['X', 'O'] # [player, bot]
    else:
        return ['O', 'X'] # [player, bot]

def choiceX():
    return ['X', 'O'] # [player, bot]

def choiceO():
    return ['O', 'X']

def printWelcome():
    menu = """
    Welcome to 'Tic-Tac-Toe'
    Please, choose your character/symbol.
    Menu:
    1. Choice X
    2. Choice O
    3. Random
    4. Input
    """
    print(menu)
    choice = 0
    while not (choice == 1 or choice == 2 or choice == 3 or choice == 4):
        choice = int(input('')) # str -> int

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


# print('Player goes', choices[0])
# print('Bot goes', choices[1])

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'Player'
    else:
        return 'Bot'


"""
 _ _ _
|1|2|3|
 - - -
|4|5|6|
 - - -
|7|8|9|
1
 _ _ _
|x|x|x|
 - - -
| | | |
 - - -
| | | |
2
 _ _ _
| | | |
 - - -
|x|x|x|
 - - -
| | | |
3
 _ _ _
| | | |
 - - -
| | | |
 - - -
|x|x|x|
4
 _ _ _
|x| | |
 - - -
|x| | |
 - - -
|x| | |
5
 _ _ _
| |x| |
 - - -
| |x| |
 - - -
| |x| |
6
 _ _ _
| | |x|
 - - -
| | |x|
 - - -
| | |x|
7
 _ _ _
|x| | |
 - - -
| |x| |
 - - -
| | |x|
8
 _ _ _
| | |x|
 - - -
| |x| |
 - - -
|x| | |
 0[1]             [9]
|-|x| | |x| | |x| | |
"""

def isWinner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or 
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter) 
    )

def makeMove(board, letter, move):
    board[move] = letter

def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    """
    -+-+-
     | |
    -+-+-
     | | 
    -+-+-
     | | 
    -+-+-
    """

def isSpaceFree(board, move):
    # board = [' ', 'x', 'o', ' ', ' ', 'x', 'o', ' ', ' ']
    # 'x'      == ' ' 
    # board[1] == ' '

    #print('Cell is not free')
    return board[move] == ' ' # ' ' == ' ' -> True


def isBoardFull(board):
    for index in range(1, 10): # index = 1, 2, 3, ...
        if isSpaceFree(board, index):
            return False
    return True


def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input('What is your next step? (1-9) : ')
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    """
    docstring
    """
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def getBotMove(board, botLetter):
    if botLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
    
    if isSpaceFree(board, 5):
        return 5
    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])




def main():
    while True:
        theBoard = [' '] * 10

        playerLetter, botLetter = printWelcome()

        turn = whoGoesFirst()
        print('\n' + turn + ' goes first.')
        gameIsPlaying = True

        while gameIsPlaying:
            # code for playing
            if turn == 'Player':
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Well, you win!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('white flag')
                        break
                    else:
                        turn = 'Bot'

            else:
                move = getBotMove(theBoard, botLetter)
                makeMove(theBoard, botLetter, move)

                if isWinner(theBoard, botLetter):
                    drawBoard(theBoard)
                    print('Bot win!')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('white flag')
                        break
                    else:
                        turn = 'Player'


        if not input('Do you want to play again? (yes/no) : ').lower().startswith('y'):
            break

if __name__ == '__main__':
    main()