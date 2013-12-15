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
        for i in range(8):
            for k in range (8):
                coord = str(k)  + str(i)
                self.board[tuple(coord)] = 'E'
        self.place_piece_at(Piece('W'), 3, 4)
        self.place_piece_at(Piece('B'), 3, 3)
        self.place_piece_at(Piece('W'), 4, 3)
        self.place_piece_at(Piece('B'), 4, 4)

    def __str__(self):
        for self.board[0] in range(8):
            for self.board[1] in range(8):
                return str(list(sorted(self.board.values())))


    def place_piece_at(self, piece, x, y):
        self.board[x,y] = piece



class Gameplay(object):
    '''Defines legal movements for pieces'''

    def __init__(self,board,player,space):
        self.board = Board()
        self.player = Piece('W')
        self.space = space


    def direct1(self,player,space,board):
        '''checks diagonal positive positive: x+1, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        for i in range(1,8):
            square1 = (self.space[1]+i,self.space[2]+i)
            if self.board[square1] == 'E':
                break
            if self.board[square1] == oppcolor:
                self.board[square1] = 'C'
                i+1
            if self.board[square1] == self.player:
                if self.board[(self.space[1]+(i-1),self.space[2]+(i-1))] == oppcolor:
                    if value == 'C':
                        value = self.player
                else:
                    break
        for value in self.board:
            if value == 'C':
                value = oppcolor


    def direct2(self,player,space,board):
        '''checks directly above: x+0, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        for i in range(1,8):
            square1 = (self.space[1],self.space[2]+i)
            if self.board[square1] == 'E':
                break
            if self.board[square1] == oppcolor:
                self.board[square1] = 'C'
                i+1
            if self.board[square1] == self.player:
                if self.board[(self.space[1],self.space[2]+(i-1))] == oppcolor:
                    if value == 'C':
                        value = self.player
                else:
                    break
        for value in self.board:
            if value == 'C':
                value = oppcolor    


    def direct3(self,player,space,board):
        '''checks diagonal negative positive: x-1, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        for i in range(1,8):
            square1 = (self.space[1]-i,self.space[2]+i)
            if self.board[square1] == 'E':
                break
            if self.board[square1] == oppcolor:
                self.board[square1] = 'C'
                i+1
            if self.board[square1] == self.player:
                if self.board[(self.space[1]-(i-1),self.space[2]+(i-1))] == oppcolor:
                    if value == 'C':
                        value = self.player
                else:
                    break
        for value in self.board:
            if value == 'C':
                value = oppcolor 


    def direct4(self,player,space,board):
        '''checks left: x-1, y+0'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        for i in range(1,8):
            square1 = (self.space[1]-i,self.space[2])
            if self.board[square1] == 'E':
                break
            if self.board[square1] == oppcolor:
                self.board[square1] = 'C'
                i+1
            if self.board[square1] == self.player:
                if self.board[(self.space[1]-(i-1),self.space[2])] == oppcolor:
                    if value == 'C':
                        value = self.player
                else:
                    break
        for value in self.board:
            if value == 'C':
                value = oppcolor 

    def empty_space(self,space):
        if self.board[space[1],space[2]] == 'E':
            pass
        else:
            return 'Sorry, that is not a valid move! Please select an empty space.'

    def __str__(self):
        return str(self.board)

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    test_game = Gameplay(Board(),'B', (3,4))
    print test_game




