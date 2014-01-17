from Tkinter import*
from localCanvassing import*


class Gameplay(object):
    '''Defines legal movements for pieces'''
 
    def __init__(self,grid):
        self.grid=grid
        self.grid.parent.title("Othello! (black's turn)")
        self.pieces_to_change = set()
        self.board = {}
        for i in range(8):
            for k in range (8):
                self.board[i,k] = 'E'
        self.board[3,4]='black'
        self.board[3,3]='white'
        self.board[4,3]='black'
        self.board[4,4]='white'
        self.playernum = 0
        self.player = 'black'
        self.event_space = 0
        print self.board

    def pre_direct(self):
        self.pieces_to_change = set()
        print 'event_space' + str(self.event_space)
        if self.event_space != 0:
            self.event_space = 0
            self.playernum += 1
            if self.playernum%2 == 1:
                self.player = 'white'
                self.grid.parent.title("Othello! (white's turn)")
            if self.playernum%2 == 0:
                self.player = 'black'
                self.grid.parent.title("Othello! (black's turn)")
            if self.player == 'black':
                self.oppcolor = 'white'
            else:
                self.oppcolor = 'black'

    def Change(self, pieces):
        for coord in pieces:
            print coord
            self.board[coord] = self.player
            self.event_space += 1
            self.pieces_to_change = set()

        print self.player

    def checkDirect(self, player, space):
        """checks all 8 directions surrounding square."""
        if self.player == 'black':
            oppcolor = 'white'
        else:
            oppcolor = 'black'
        if self.board[space] == 'E': # checks if space is empty (available)
            for x in range(-1,2): 
                for y in range(-1,2):
                    self.pieces_to_change = set() # make empty set to hold 'flippable' pieces
                    for i in range(1,8):
                        # makes sure not to check past edges
                        if space[0]+(x*i) == 8 or space[0]+(x*i) == -1: # right
                            break
                        if space[1]+(y*i) == -1 or space[1]+(y*i) == 8: # left
                            break
                        # test adjacent coordinates
                        if self.board[(space[0]+(x*i)),(space[1]+(y*i))] == oppcolor:
                            self.pieces_to_change.add(((space[0]+(x*i)),(space[1]+(y*i)))) # add to flip list
                        if self.board[(space[0]+(x*i)),(space[1]+(y*i))] == 'E':
                            self.pieces_to_change = set() # reset flip list
                            break
                        if self.board[(space[0]+(x*i)),(space[1]+(y*i))] == self.player:
                            if i >= 2: # assure that an oppcolor was in between
                                self.Change(self.pieces_to_change) # flip pieces
                                break
                            else:
                                break
        print self.board[space]

    def fill_event(self,space):
        print 'fill'
        if self.event_space >= 1:
            self.board[space] = self.player

    def updateBoard(self,coordinate):
        self.checkDirect(self.player,coordinate)
        self.fill_event(coordinate)
        self.pre_direct()
        self.grid.makeBoard()
        print self.board
        black = 0
        white = 0
        for coordinates, value in self.board.items():
            if value == "black":
                black += 1
            elif value == "white":
                white += 1
        print 'black:' + str(black)
        print 'white:' + str(white)

if __name__ == "__main__":
    root = Tk()
    gui = Board(root)
    root.mainloop()
