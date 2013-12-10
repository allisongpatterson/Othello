class Piece(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color

    def flip(self):
        if self.color == 'W':
            self.color = 'B'
        if self.color == 'B':
            self.color = 'W'

class Board(object):
    def __init__(self):
        self.board = {}
        alpha = list('01234567')
        for i in range(8):
            for k in range (8):
                coord = alpha[k]  + str(i)
                self.board[tuple(coord)] = 'E'
        self.place_piece_at(Piece('W'), 3, 4)
        self.place_piece_at(Piece('B'), 3, 3)
        self.place_piece_at(Piece('W'), 4, 3)
        self.place_piece_at(Piece('B'), 4, 4)

    def __str__(self):
        for self.board[1] in range(8):
            for 
        #for coordinates in self.board:
            #for x in coordinates:
                #for x in range(8):
                    #if x == 1
        return str(self.board.values())

    def place_piece_at(self, piece, x, y):
        self.board[x,y] = piece



# class Gameplay(object):
#     '''Defines legal movements for pieces'''

#     def __init__(self,piece,board,player):
#         self.piece = piece
#         self.board = board
#         self.player = player

#     def diag_pos(self,player,space,board):
#         '''checks diagonal up'''
#         if self.player == 'B':
#             oppcolor = 'W'
#         else:
#             oppcolor = 'B'
#         for i in range(1,8):
#             self.diag_pos = (space[1]+i,space[2]+i)
#             if board[self.diag_pos] == 'E':
#                 break
#             if board[self.diag_pos] == oppcolor:
                
#             if board[self.diag_pos] == self.player:
#                 flip

#     def empty_space(self,space):
#         if self.board[space[1],space[2]] == 'E':
#         else:
#             return 'Sorry, that is not a valid move! Please select an empty space.'


if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    test_board = Board()
    print test_board






