import random
from check import *
from get import *
from medium_move import *

global coords
initial_board = [' ', ' ', ' ',
                 ' ', ' ', ' ',
                 ' ', ' ', ' ']


def get_board(command):
    coordinates = {'1 1': initial_board[6], '1 2': initial_board[3], '1 3': initial_board[0],
                   '2 1': initial_board[7], '2 2': initial_board[4], '2 3': initial_board[1],
                   '3 1': initial_board[8], '3 2': initial_board[5], '3 3': initial_board[2]}

    print(f"""---------
| {coordinates['1 3']} {coordinates['2 3']} {coordinates['3 3']} |
| {coordinates['1 2']} {coordinates['2 2']} {coordinates['3 2']} |
| {coordinates['1 1']} {coordinates['2 1']} {coordinates['3 1']} |
---------""")

    if 'user' in command:
        play(coordinates, command)
    else:
        compvscomp(coordinates, command)


def update_board(board):
    print(f"""---------
| {board['1 3']} {board['2 3']} {board['3 3']} |
| {board['1 2']} {board['2 2']} {board['3 2']} |
| {board['1 1']} {board['2 1']} {board['3 1']} |
---------""")


def num_of(board):
    number_of_x = 0
    number_of_o = 0
    for i in board:
        if board[i] == 'X':
            number_of_x += 1
        elif board[i] == 'O':
            number_of_o += 1
    return number_of_x, number_of_o


def computer_move_easy(board):
    while True:
        move = random.choice(list(board.keys()))
        if board[move] == ' ':
            return move


def computer_move_medium(board, char):
    return medium_func(board, char)


def play(board, command):
    global coords
    turn = 0
    while True:
        num_x, num_o = num_of(board)
        if num_x == num_o:
            char = 'X'
        else:
            char = 'O'
        if command[1] == 'user':
            if command[2] == 'easy':
                if turn % 2 == 0:
                    coords = input('Enter the coordinates: ')
                else:
                    coords = computer_move_easy(board)
                    print('Making move level "easy"')
            elif command[2] == 'medium':
                if turn % 2 == 0:
                    coords = input('Enter the coordinates: ')
                else:
                    coords = computer_move_medium(board, char)
                    print('Making move level "medium"')
            else:
                coords = input('Enter the coordinates: ')
        elif command[1] == 'easy':
            if turn % 2 == 0:
                coords = computer_move_easy(board)
                print('Making move level "easy"')
            else:
                coords = input('Enter the coordinates: ')
        elif command[1] == 'medium':
            if turn % 2 == 0:
                coords = computer_move_medium(board, char)
                print('Making move level "medium"')
            else:
                coords = input('Enter the coordinates: ')
        if not check_input_words(coords):
            if check_input(coords):
                if board[coords] == ' ':
                    board[coords] = char
                    turn += 1
                    update_board(board)
                    if not check_win(board):
                        if check_diagonals(board):
                            print(f'{board[coords]} wins\n')
                            break
                        else:
                            if check_draw(board):
                                print('Draw\n')
                                break
                    else:
                        print(f'{board[coords]} wins\n')
                        break
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


def compvscomp(board, command):
    global coords
    turn = 0
    while True:
        num_x, num_o = num_of(board)
        if num_x == num_o:
            char = 'X'
        else:
            char = 'O'
        if command[1] == 'easy':
            if command[2] == 'easy':
                if turn % 2 == 0:
                    coords = computer_move_easy(board)
                    print('Making move level "easy"')
                else:
                    coords = computer_move_easy(board)
                    print('Making move level "easy"')
            elif command[2] == 'medium':
                    if turn % 2 == 0:
                        coords = computer_move_easy(board)
                        print('Making move level "easy"')
                    else:
                        coords = computer_move_medium(board, char)
                        print('Making move level "medium"')
        elif command[1] == 'medium':
            if command[2] == 'easy':
                if turn % 2 == 0:
                    coords = computer_move_medium(board, char)
                    print('Making move level "medium"')
                else:
                    coords = computer_move_easy(board)
                    print('Making move level "easy"')
            elif command[2] == 'medium':
                if turn % 2 == 0:
                    coords = computer_move_medium(board, char)
                    print('Making move level "medium"')
                else:
                    coords = computer_move_medium(board, char)
                    print('Making move level "medium"')
        if board[coords] == ' ':
            board[coords] = char
            turn += 1
            update_board(board)
            if not check_win(board):
                if check_diagonals(board):
                    print(f'{board[coords]} wins\n')
                    break
                else:
                    if check_draw(board):
                        print('Draw\n')
                        break
            else:
                print(f'{board[coords]} wins\n')
                break

def menu():
    while True:
        command = input('Input command: ').split(" ")
        if len(command) <= 2:
            if command[0] == 'exit':
                break
            else:
                print('Bad parameters!')
        elif len(command) > 2:
            if command[2] == 'hard':
                print('Bad parameters!')
            elif command[1] == 'hard':
                print('Bad parameters!')
            else:
                get_board(command)
        else:
            print('Bad parameters!')


if __name__ == "__main__":
    menu()
       

