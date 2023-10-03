class Board:
    def __init__(self):
        self.board = []

    def boards(self):
        for index in range(3):
            row = []
            for index2 in range(3):
                row.append('~')
            self.board.append(row)
