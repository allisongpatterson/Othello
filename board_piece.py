class Piece(object):
    def __init__(self, color):
        self.color = color

    def flip(self):
        if self.color == 'W':
            self.color = 'B'
        if self.color == 'B':
            self.color = 'W'

class Board(object):
    def __init__(self):
        self.board = {}
        alpha = list('12345678') #changed to numbers instead 
        for i in range(1,9):
            for k in range (8):
                coord = alpha[k]  + str(i)
                board[tuple(coord)] = 'E'
        self.place_piece_at(Piece('W'), 3, 4)
        self.place_piece_at(Piece('B'), 3, 3)
        self.place_piece_at(Piece('W'), 4, 3)
        self.place_piece_at(Piece('B'), 4, 4)
        return self.board

    def place_piece_at(self, piece, x, y):
        self.board[x, y] = piece

     def look_right(self, x, y):


b = Board()
print b
