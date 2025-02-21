class Square:

    def __init__(self, row, col, number = None, piece = None):
        self.row = row
        self.col = col
        self.number = number
        self.piece = piece

    def has_piece(self):
        return self.piece != None



