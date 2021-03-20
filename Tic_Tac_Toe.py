import random


def display_board(board):
    row1 = [ board[1], board[2], board[3]]
    row2 = [ board[4], board[5], board[6]]
    row3 = [ board[7], board[8], board[9]]

    matrix = [row1, row2, row3]
    print('\n'*100)
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])



test_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#display_board(test_board)


def player_input():
    a=''
    b=True
    while b:
        a = input(" Please pick a marker 'X' or 'O' ").upper()
        if a=='X'or a=='O':
            b=False
    while not b:
        if a=='X':
            return ('X','O')
        else:
            return ('O','X')


#print(player_input())

def place_marker(board,marker,position):
    board[position] = marker

#Manually added items to the Board
#place_marker(test_board,'X',1)
#place_marker(test_board,'X',2)
#place_marker(test_board,'X',3)
#place_marker(test_board,'X',4)
#place_marker(test_board,'X',5)
#place_marker(test_board,'X',6)
#place_marker(test_board,'X',7)
#place_marker(test_board,'X',8)
#place_marker(test_board,'X',9)
#display_board(test_board)


def win_check(board,mark):
    #Possibilities of wining
    opt1 = [board[1], board[2], board[3]]
    opt2 = [board[4], board[5], board[6]]
    opt3 = [board[7], board[8], board[9]]
    opt4 = [board[1], board[4], board[7]]
    opt5 = [board[2], board[5], board[8]]
    opt6 = [board[3], board[6], board[9]]
    opt7 = [board[1], board[5], board[9]]
    opt8 = [board[3], board[5], board[7]]
    win = [opt1,opt2,opt3,opt4,opt5,opt6,opt7,opt8]

    if (win[0].count(mark)==3 or win[1].count(mark)==3 or win[2].count(mark)==3 or win[3].count(mark)==3 or win[4].count(mark)==3 or win[5].count(mark)==3 or win[6].count(mark)==3 or  win[7].count(mark)==3):
        return True
    else:
        return False

#print(win_check(test_board,'X'))


def choose_first():
    a=random.randint(1,2)
    if a==1:
        return 'Player 1 starts'
    else:
        return 'Player 2 starts'


#print(choose_first())

def space_check(board,position):

    if board[position]=='X' or board[position]=='O':
        return False
    else:
        return True


#print(space_check(test_board,1))

def full_board_check(board):
    c=0
    b=False
    for i in board[1::]:
        if i=='X' or i=='O':
            c+=1

        if c==9:
            b=True


    while b:
        return True


    while not b:
        return False


#print(full_board_check(test_board))


def player_choice(board):

    pos = int(input("What position next? : "))

    if space_check(board,pos):
        return pos
    else:
        print('Try again')
        return(player_choice(board))



#print(player_choice(test_board))


def replay():
    again = input("Do you want to play again? (y/n)")

    if again =='y':
        return True
    elif again =='n':
        return False
    else:
        print('Invalid character,type y or n')
        return replay()

#print(replay())


##### MAIN #######

print('Welcome to Tic Tac Toe!')

while True:
    Board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player1,player2 = player_input()
    tura = choose_first()
    print(tura)

    start = input("People are you ready? (y/n)")
    if start == 'y':
        on = True
    else:
        on = False

    while on:
        if tura == "Player 1 starts":
            display_board(Board)
            pos = player_choice(Board)
            place_marker(Board,player1,pos)

            if win_check(Board,player1):
                display_board(Board)
                print('Player 1 wins')
                on = False
            else:
                if full_board_check(Board):
                    display_board(Board)
                    print("Draw!")
                    break
                else:
                    tura = 'Player 2 starts'

        else:
            display_board(Board)
            pos = player_choice(Board)
            place_marker(Board,player2,pos)

            if win_check(Board,player2):
                display_board(Board)
                print('Player 2 wins')
                on = False

            else:
                if full_board_check(Board):
                    display_board(Board)
                    print('Draw!')
                    break

                else:
                    tura = 'Player 1 starts'

    if not replay():
        break














