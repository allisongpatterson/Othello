<<<<<<< HEAD
from Tkinter import*
from canvassing import*
=======
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81

class Gameplay(object):
    '''Defines legal movements for pieces'''
 
    def __init__(self):
<<<<<<< HEAD
        self.restart()

    def restart(self):
        self.player = 'black'
=======
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
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
<<<<<<< HEAD
        self.board[('3','4')]='black'
        self.board[('3','3')]='white'
        self.board[('4','3')]='black'
        self.board[('4','4')]='white'

    def direct1(self,player,space, testing = None):
        self.testing = 5
        print self.player
        '''checks diagonal positive positive (northeast): x+1, y-1'''
        if self.player == 'black':
            oppcolor = 'white'
=======
        self.board[('3','4')]='B'
        self.board[('3','3')]='W'
        self.board[('4','3')]='B'
        self.board[('4','4')]='W'
        print 'restart'
        self.playernum = 1

    # def load_pickle(self):
    #     import pickle
    #     print 'in pickle'
    #     self.board = pickle.load( open( "save.p", "rb"))

    def pre_direct(self,board):
        if self.playernum%2 == 0:
            self.player = 'W'
        if self.playernum%2 == 1:
            self.player = 'B'
        else:
            return "ERROR: PLAYER-PREDIRECT"
        return self.player

    def direct1(self,player,space):
        '''checks diagonal positive positive (northeast): x+1, y-1'''
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
        else:
            oppcolor = 'black'
        return space[0]
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 7:
                    break
                if space[1] == 7:
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
                                self.a = 1
            for value in self.board:
                if value == 'C':
                    value = oppcolor
        print 'direct1'
        print self.a
        print self.board[str(space[0]),str(space[1])]

    def direct2(self,player,space):
        '''checks upward(north): x+0, y-1'''
<<<<<<< HEAD
        if self.player == 'black':
            oppcolor = 'white'
            print 'oppcolor white'
=======
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.b = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct2'
        print self.b
        print self.board[str(space[0]),str(space[1])]

    def direct3(self,player,space):
        '''checks diagonal negative positive (northwest): x-1, y-1'''
<<<<<<< HEAD
        if self.player == 'black':
            oppcolor = 'white'
=======
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.c = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.d = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct4'
        print self.d
        print self.board[str(space[0]),str(space[1])]

    def direct5(self,player,space):
        '''checks diagonal negative negative (southwest): x-1, y+1'''
<<<<<<< HEAD
        if self.player == 'black':
            oppcolor = 'white'
=======
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
        else:
            oppcolor = 'black'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if space[0] == 0:
                    break
                if space[1] == 0:
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
                                self.e = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct5'
        print self.e
        print self.board[str(space[0]),str(space[1])]

    def direct6(self,player,space):
        '''checks downward (south): x+0, y+1'''
<<<<<<< HEAD
        if self.player == 'black':
            oppcolor = 'white'
=======
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.f = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct6'
        print self.f
        print self.board[str(space[0]),str(space[1])]

    def direct7(self,player,space):
        '''checks diagonal positive negative (southeast): x+1, y+1'''
<<<<<<< HEAD
        if self.player == 'black':
            oppcolor = 'white'
=======
        if self.player == 'B':
            oppcolor = 'W'
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.g = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
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
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = self.player
                                self.board[str(space[0]),str(space[1])] = self.player
                                self.h = 1
        for value in self.board:
            if value == 'C':
                value = oppcolor
        print 'direct8'
<<<<<<< HEAD

    def switch_player(self,last_player):
        if last_player == 'black':
            self.player = 'white'
        else:
            self.player = 'black'
        return self.player
=======
        print self.h
        print self.board[str(space[0]),str(space[1])]
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81

    def empty_space(self,space,player):
        #print self.b
        # return self.player_number
        if self.a + self.b + self.c + self.d + self.e + self.f + self.g + self.h != 0:
        #if self.board[str(space[0]),str(space[1])] == self.player:
            self.playernum += 1
            self.a = 0
            self.b = 0
            self.c = 0
            self.d = 0
            self.e = 0
            self.f = 0
            self.g = 0
            self.h = 0
            return self.playernum
        else:
            return 'Sorry, that is not a valid move! Please select another space.'
    
    # def save_pickle(self,board):
    #     import pickle
    #     pickle.dump(self.board, open('save.p', 'wb'))

    # def __str__(self):
    #     return str(self.board)

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    
   
    root = Tk()
    gui = Board(root)
    root.mainloop()
    test_game = Gameplay()
<<<<<<< HEAD
    #coordinate = gui.point
    #print gui.point
    #print test_game.board[('3', '4')]
    
    # test_game.restart
    
    print test_game.direct1(test_game.player,('7','7'))
    # test_game.direct2(test_game.player,coordinate)
    # test_game.direct3(test_game.player,coordinate)
    # test_game.direct4(test_game.player,coordinate)
    # test_game.direct5(test_game.player,coordinate)
    # test_game.direct6(test_game.player,coordinate)
    # test_game.direct7(test_game.player,coordinate)
    # test_game.direct8(test_game.player,coordinate)
=======
    #print test_game.board
    coordinate = (5,4)
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81
    
    # test_game.load_pickle()
    print test_game.pre_direct(test_game.board)
    print test_game.direct1(test_game.player,coordinate)
    print test_game.direct2(test_game.player,coordinate)
    print test_game.direct3(test_game.player,coordinate)
    print test_game.direct4(test_game.player,coordinate)
    print test_game.direct5(test_game.player,coordinate)
    print test_game.direct6(test_game.player,coordinate)
    print test_game.direct7(test_game.player,coordinate)
    print test_game.direct8(test_game.player,coordinate)
    # test_game.save_pickle(test_game.board)    

    # print test_game.empty_space(coordinate,test_game.player)
    # print test_game.board

<<<<<<< HEAD
    # print test_game.empty_space(coordinate,test_game.player)
    #print test_game.board
 
=======
>>>>>>> 70296fd25e6c3d055f104f92f3e158a2a4be4b81




