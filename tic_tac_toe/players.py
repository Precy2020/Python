import random

from tic_tac_toe.board import Board


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X' \
            if random.randint(0, 1) == 1 else 'O'

    def switch_player(self):
        self.current_player = 'X'\
            if self.current_player == 'O' else 'O'

    def make_move(self, row, column):
        self.board.board[row][column] = self.current_player

    def check_winner(self):
        player = self.current_player
        number = len(self.board.board)

        for row in range(number):
            if all(self.board.board[row][column] == player for column in range(number)) or \
                    all(self.board.board[column][row] == player for column in range(number)):
                return True

        if all(self.board.board[row][row] == player for row in range(number)) or \
                all(self.board.board[row][number - 1 - row] == player for row in range(number)):
            return True

        return False

    def check_if_board_is_full(self):
        return all(item != '-' for row in self.board.board for item in row)

    def play(self):
        while True:
            print(f"Player {self.current_player} turn")
            self.board.boards()

            row, column = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            if self.board.board[row - 1][column - 1] == '-':
                self.make_move(row - 1, column - 1)

                if self.check_winner():
                    print(f"Player {self.current_player} wins the game!")
                    break

                if self.check_if_board_is_full():
                    print("Match Draw!")
                    break

                self.switch_player()
            else:
                print("Invalid move. Try again.")


tic_tac_toe_game = TicTacToeGame()
tic_tac_toe_game.play()
