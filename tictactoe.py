from os import system


def print_instructions():
    '''Instruction how to play the game.'''
    print('\nWelcome to Tic-Tac-Toe!')
    print('\nEach squares in the board is represented by numbers.')
    print('Select the number in which you want to put your mark on.')
    print_grid()
    print('-----------')
    print_board(ttt_board)


def print_grid():
    '''Board grid pattern.'''
    print('\n 1 | 2 | 3 \n - + - + - \n 4 | 5 | 6 \n - + - + - \n 7 | 8 | 9 \n')


def print_board(b):
    '''Print the tic tac toe board.'''
    # b as board
    print()
    print(f' {b[1]} | {b[2]} | {b[3]} ')
    print(' - + - + - ')
    print(f' {b[4]} | {b[5]} | {b[6]} ')
    print(' - + - + - ')
    print(f' {b[7]} | {b[8]} | {b[9]} ')


def print_board_and_grid():
    '''Print the board and grids(for guide) together.'''
    print_grid()
    print('-----------')
    print_board(ttt_board)


def is_empty(board, grid):
    '''Check if grid is empty.'''
    if board[grid] != ' ':
        return False
    else:
        return True


def winner(b, player):
    '''Check if player wins.'''
    R1 = b[1] == b[2] == b[3] == player
    R2 = b[4] == b[5] == b[6] == player
    R3 = b[7] == b[8] == b[9] == player
    C1 = b[1] == b[4] == b[7] == player
    C2 = b[2] == b[5] == b[8] == player
    C3 = b[3] == b[6] == b[9] == player
    D1 = b[1] == b[5] == b[9] == player
    D2 = b[3] == b[5] == b[7] == player
    return  R1 or R2 or R3 or C1 or C2 or C3 or D1 or D2


ttt_board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}


def main():
    '''Main program.'''
    system('clear')
    print_instructions()

    player = 'X'
    turn_count = 0

    while True:
        turn = input(f"\nPlayer {player}'s turn.\nSelect a grid: ")
        if not turn.isdigit():
            system('clear')
            print('Please select a number from 1 - 9.')
            print_board_and_grid()

        else:
            turn = int(turn)
            if 0 < turn < 10:

                if is_empty(ttt_board, turn):
                    ttt_board[turn] = player
                    system('clear')
                    print_board_and_grid()

                    if winner(ttt_board, player):
                        print(f'\nGame over!\nPlayer {player} wins!')
                        break

                    if player == 'X': player = 'O'
                    else: player = 'X'

                    turn_count += 1

                else:
                    system('clear')
                    print(f'Oops!\nGrid {turn} already taken.')
                    print_board_and_grid()

            else:
                system('clear')
                print('Please select a number from 1 - 9.')
                print_board_and_grid()

            if turn_count >= 9:
                print("\nGame over!\nIt's a draw.")
                break


if __name__ == '__main__':
    main()
