# class Board(object):
#     def __init__(self):
#         self.newboard = None
#         self.board = {}
#         for i in range(8):
#             for k in range (8):
#                 coord = str(k)  + str(i)
#                 self.board[tuple(coord)] = 'E'
#         self.place_piece_at('W', '3', '4')
#         self.place_piece_at('B', '3', '3')
#         self.place_piece_at('W', '4', '3')
#         self.place_piece_at('B', '4', '4')

#     def __str__(self):
#         for self.board[0] in range(8):
#             for self.board[1] in range(8):
#                 return str(self.board)


#     def place_piece_at(self, piece, x, y):
#         self.board[x,y] = piece



class Gameplay(object):
    '''Defines legal movements for pieces'''

 

    def __init__(self):
        self.restart()

    def restart(self):
        self.testing = 3
        self.player = 'B'
        self.board = {}
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0
        self.g = 0
        self.h = 0
        for i in range(8):
            for k in range (8):
                self.coord = str(k)  + str(i)
                self.board[tuple(self.coord)] = 'E'
        self.board[('3','4')]='W'
        self.board[('3','3')]='B'
        self.board[('4','3')]='W'
        self.board[('4','4')]='B'

    def direct1(self,player,space):
        print self.player
        '''checks diagonal positive positive (northeast): x+1, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if space[1] == 7:
                    break
                if self.board[str(space[0]+i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]+(i-1)),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.a = 1
            for value in self.board:
                if value == 'C':
                    value = oppcolor
        print 'direct1'

    def direct2(self,player,space):
        '''checks upward(north): x+0, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
            print 'oppcolor W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[1] == '7':
                    return
                if self.board[str(space[0]),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]+i)] = 'C'
                if self.board[str(space[0]),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                print self.board[key]
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.b = 1
                                return
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct2'

    def direct3(self,player,space):
        '''checks diagonal negative positive (northwest): x-1, y+1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if space[1] == 7:
                    break
                if self.board[str(space[0]-i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]-i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]-(i-1)),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.c = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct3'


    def direct4(self,player,space):
        '''checks left(west): x-1, y+0'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if self.board[str(space[0]-i),str(space[1])] == oppcolor:
                    self.board[str(space[0]-i),str(space[1])] = 'C'
                if self.board[str(space[0]-i),str(space[1])] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1])] == self.player:
                    if self.board[str(space[0]-(i-1)),str(space[1])] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.d = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct4'

    def direct5(self,player,space):
        '''checks diagonal negative negative (southwest): x-1, y-1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if space[1] == 0:
                    break
                if self.board[str(space[0]-i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]-i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]-(i-1)),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.e = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct5'

    def direct6(self,player,space):
        '''checks downward (south): x+0, y-1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[1] == 0:
                    break
                if self.board[str(space[0]),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]-i)] = 'C'
                if self.board[str(space[0]),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.f = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct6'

    def direct7(self,player,space):
        '''checks diagonal positive negative (southeast): x+1, y-1'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if space[1] == 0:
                    break
                if self.board[str(space[0]+i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]+(i-1)),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.g = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct7'

    def direct8(self,player,space):
        '''checks right (east): x+1, y+0'''
        if self.player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if self.board[str(space[0]+i),str(space[1])] == oppcolor:
                    self.board[str(space[0]+i),str(space[1])] = 'C'
                if self.board[str(space[0]+i),str(space[1])] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1])] == self.player:
                    if self.board[str(space[0]+(i-1)),str(space[1])] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.h = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct8'

    def switch_player(self,last_player):
        if last_player == 'B':
            self.player = 'W'
        else:
            self.player = 'B'
        return self.player

    def empty_space(self,space,player):
        #print self.b
        if self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h != 0:
        #if self.board[str(space[0]),str(space[1])] == self.player:
            self.switch_player(self.player)
            self.a = 0
            self.b = 0
            self.c = 0
            self.d = 0
            self.e = 0
            self.f = 0
            self.g = 0
            self.h = 0
            print self.player
            return self.player
        else:
            return 'Sorry, that is not a valid move! Please select another space.'

    def __str__(self):
        return str(self.board)

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    test_game = Gameplay()
    coordinate = (3,2)
    
    #test_game.restart
    
    test_game.direct1(test_game.player,coordinate)
    test_game.direct2(test_game.player,coordinate)
    test_game.direct3(test_game.player,coordinate)
    test_game.direct4(test_game.player,coordinate)
    test_game.direct5(test_game.player,coordinate)
    test_game.direct6(test_game.player,coordinate)
    test_game.direct7(test_game.player,coordinate)
    test_game.direct8(test_game.player,coordinate)#
    


    print test_game.empty_space(coordinate,test_game.player)
    print test_game.board




