class Board(object):
    def __init__(self):
        self.board = {}
        for i in range(8):
            for k in range (8):
                coord = str(k)  + str(i)
                self.board[tuple(coord)] = 'E'
        self.place_piece_at('W', '3', '4')
        self.place_piece_at('B', '3', '3')
        self.place_piece_at('W', '4', '3')
        self.place_piece_at('B', '4', '4')
        self.place_piece_at('W', '5', '5')

    def __str__(self):
        for self.board[0] in range(8):
            for self.board[1] in range(8):
                return str(self.board)


    def place_piece_at(self, piece, x, y):
        self.board[x,y] = piece



class Gameplay(object):
    '''Defines legal movements for pieces'''

    def __init__(self):
        self.board = Board().board


    def direct1(self,player,space):
        '''checks diagonal positive positive (northeast): x+1, y+1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        return type(self.board)
        if self.board[(space[0]),(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]+i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]+i)] == player: #why i-1?
                    if self.board[str(space[0]+(i-1)),str(space[1]+(i-1))] == 'C':
                        if self.board.value == 'C':
                            value = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    # def direct2(self,player,space,board):
    #     '''checks directly above (north): x+0, y+1'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         if self.board[self.space] == 'E':
    #             break
    #         if self.board[self.space] == oppcolor:
    #             self.board[self.space] = 'C'
    #             i+1
    #         if self.board[self.space] == self.player:
    #             if self.board[(self.space[1],self.space[2]+(i-1))] == oppcolor: #why i-1?
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor    


    # def direct3(self,player,space,board):
    #     '''checks diagonal negative positive (northwest): x-1, y+1'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1]-i,self.space[2]+i)
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1]-(i-1),self.space[2]+(i-1))] == oppcolor:
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor 


    # def direct4(self,player,space,board):
    #     '''checks left (west): x-1, y+0'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1]-i,self.space[2])
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1]-(i-1),self.space[2])] == oppcolor:
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor 

    #  def direct5(self,player,space,board):
    #     '''checks right (east): x+1, y+0'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1]+i,self.space[2])
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1]+(i-1),self.space[2])] == oppcolor:
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor

    # def direct6(self,player,space,board):
    #     '''checks diagonal negative negative (southwest): x-1, y-1'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1]-i,self.space[2]-i)
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1]-(i-1),self.space[2]-(i-1))] == oppcolor:
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor 


    # def direct7(self,player,space,board):
    #     '''checks diagonal positive negative (southeast): x+1, y-1'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1]+i,self.space[2]-i)
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1]+(i-1),self.space[2]-(i-1))] == oppcolor:
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor 

    # def direct8(self,player,space,board):
    #     '''checks directly below (south): x+0, y-1'''
    #     if self.player == 'B':
    #         oppcolor = 'W'
    #     else:
    #         oppcolor = 'B'
    #     for i in range(1,8):
    #         square1 = (self.space[1],self.space[2]-i)
    #         if self.board[square1] == 'E':
    #             break
    #         if self.board[square1] == oppcolor:
    #             self.board[square1] = 'C'
    #             i+1
    #         if self.board[square1] == self.player:
    #             if self.board[(self.space[1],self.space[2]-(i-1))] == oppcolor: #why i-1?
    #                 if value == 'C':
    #                     value = self.player
    #             else:
    #                 break
    #     for value in self.board:
    #         if value == 'C':
    #             value = oppcolor 

    def empty_space(self,space):
        if self.board[space[1],space[2]] == 'E':
            pass
        else:
            return 'Sorry, that is not a valid move! Please select an empty space.'

    def __str__(self):
        return str(sorted(self.board))

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    test_game = Gameplay()
    test_game.direct1('W',(2,2))
    print test_game



