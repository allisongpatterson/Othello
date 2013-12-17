
from Tkinter import*
from canvassing import*


class Gameplay(object):
    '''Defines legal movements for pieces'''
 
    def __init__(self,grid):
        self.grid=grid
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
        self.board[('3','4')]='black'
        self.board[('3','3')]='white'
        self.board[('4','3')]='black'
        self.board[('4','4')]='white'
        self.playernum = 1
        print 'Initializing.'

    def pre_direct(self):
        if self.playernum%2 == 0:
            self.player = 'white'
        if self.playernum%2 == 1:
            self.player = 'black'

        #return self.player

    def direct1(self,player,space):
        '''checks diagonal positive positive (northeast): x+1, y-1'''
        print self.player
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if space[1] == 7:
                    break
                if self.board[str(space[0]+i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]-i)] == 'E':
                    print 'breaking empty'
                    break 
                if self.board[str(space[0]+i),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]+(i-1)),str(space[1]-(i-1))] == 'C':
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.a = 1
        print 'going'
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct1'
        print self.a
        print self.board[str(space[0]),str(space[1])]

    def direct2(self,player,space):
        '''checks upward(north): x+0, y-1'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[1] == '7':
                    return
                if self.board[str(space[0]),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]-i)] = 'C'
                if self.board[str(space[0]),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]),str(space[1]-(i-1))] == 'C':
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.b = 1
        #print 'going'
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct2'
        print self.b
        print self.board[str(space[0]),str(space[1])]

    def direct3(self,player,space):
        '''checks diagonal negative positive (northwest): x-1, y-1'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if space[1] == 7:
                    break
                if self.board[str(space[0]-i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]-i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1]-i)] == self.player:
                    if self.board[str(space[0]-(i-1)),str(space[1]-(i-1))] == 'C':
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.c = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct3'
        print self.c
        print self.board[str(space[0]),str(space[1])]


    def direct4(self,player,space):
        '''checks left(west): x-1, y+0'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
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
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.d = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct4'
        print self.d
        print self.board[str(space[0]),str(space[1])]

    def direct5(self,player,space):
        '''checks diagonal negative negative (southwest): x-1, y+1'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if space[1] == 0:
                    break
                if self.board[str(space[0]-i),str(space[1]+i)] == oppcolor:
                    print 'making a C'
                    self.board[str(space[0]-i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]+i)] == 'E':
                    print 'breaking empty'
                    break 
                if self.board[str(space[0]-i),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]-(i-1)),str(space[1]+(i-1))] == 'C':
                        print 'need to change C'
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                print 'Changed C'
                                self.board[str(x),str(y)] = self.player
                                self.e = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct5'
        print self.e
        print self.board[str(space[0]),str(space[1])]

    def direct6(self,player,space):
        '''checks downward (south): x+0, y+1'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[1] == 0:
                    break
                if self.board[str(space[0]),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]+i)] = 'C'
                if self.board[str(space[0]),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]),str(space[1]+(i-1))] == 'C':
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.f = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct6'
        print self.f
        print self.board[str(space[0]),str(space[1])]

    def direct7(self,player,space):
        '''checks diagonal positive negative (southeast): x+1, y+1'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if space[1] == 0:
                    break
                if self.board[str(space[0]+i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]+i)] == self.player:
                    if self.board[str(space[0]+(i-1)),str(space[1]+(i-1))] == 'C':
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.g = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct7'
        print self.g
        print self.board[str(space[0]),str(space[1])]

    def direct8(self,player,space):
        '''checks right (east): x+1, y+0'''
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
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
                        for x, y in self.board:
                            if self.board[str(x),str(y)] == 'C':
                                self.board[str(x),str(y)] = self.player
                                self.h = 1
        for x, y in self.board:
            if self.board[str(x),str(y)] == 'C':
                if self.board[str(x),str(y)] == 'C':
                    self.board[str(x),str(y)]= oppcolor
        print 'direct8'
        print self.h
        print self.board[str(space[0]),str(space[1])]


    def empty_space(self,space,player):
        #print self.b
        # return self.player_number
        if self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h != 0:
        #if self.board[str(space[0]),str(space[1])] == self.player:
            self.board[str(space[0]),str(space[1])] = self.player
            self.playernum += 1
            self.a = 0
            self.b = 0
            self.c = 0
            self.d = 0
            self.e = 0
            self.f = 0
            self.g = 0
            self.h = 0
            print self.playernum
        else:
            return 'Sorry, that is not a valid move! Please select another space.'
    
    # def save_pickle(self,board):
    #     import pickle
    #     pickle.dump(self.board, open('save.p', 'wb'))

    # def __str__(self):
    #     return str(self.board)
    def updateBoard(self,coordinate):
        print self.pre_direct()
        print self.direct1(self.player,coordinate)
        print self.direct2(self.player,coordinate)
        print self.direct3(self.player,coordinate)
        print self.direct4(self.player,coordinate)
        print self.direct5(self.player,coordinate)
        print self.direct6(self.player,coordinate)
        print self.direct7(self.player,coordinate)
        print self.direct8(self.player,coordinate)
        print self.empty_space(coordinate,self.player)
        self.grid.makeBoard()
        #print self.board

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    
   

    root = Tk()
    gui = Board(root)
    root.mainloop()

    print("done looping")

    #coordinate = gui.point
    #print coordinate


   

    #test_game.empty_space(coordinate,test_game.player)
    # print test_game.board



