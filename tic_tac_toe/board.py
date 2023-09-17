class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def show_board(self):
        for row in self.board:
            print("!".join(row))
            print("<><><>")

    def move(self, rows, columns, player_symbol):
        if self.is_valid_move(rows, columns):
            self.board[rows][columns] = player_symbol
        else:
            print("Invalid move. Try again.")

    def is_valid_move(self, rows, columns):
        if 0 <= rows < 3 and 0 <= columns < 3 and self.board[rows][columns] == " ":
            return True
        return False


board = Board()
board.show_board()

print(board)
