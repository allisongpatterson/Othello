from Tkinter import*
from canvassing1 import*
import sys
import json
import urllib2
import time

class Gameplay(object):
    '''Defines legal movements for pieces'''
 
    def __init__(self,grid):
        self.gameName = sys.argv[1]
        self.playerColor = sys.argv[2]
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
        self.event_space = 0
        self.pre_direct()
        self.updateFromServer()
        print self.board

    def updateFromServer(self):
        status = self.getCurrentStatus()
        if status[1] == 'black':
            print 'update black'
            self.player = 'white'
            self.playernum = 1
            if status[0][0] != 4 or status[0][1] != 4: # make sure last move was not on 4,4 (starting square)
                print 'yes'
                self.checkDirect('white', (status[0][0],status[0][1])) # displays last move's flips
                self.board[status[0][0],status[0][1]]='white' # fills last player's space w/ proper color
            self.playernum = 0
            self.player = 'black'
        elif status[1] == 'white':
            print 'update white'
            self.playernum = 0
            self.player = 'black'
            self.checkDirect('black', (status[0][0],status[0][1])) # displays last move's flips
            self.board[status[0][0],status[0][1]]='black' # fills last player's space w/ proper color
            self.playernum = 1
            self.player = 'white'
        print self.board

    def getCurrentStatus(self): # talk to server
        req = urllib2.Request('http://othello.herokuapp.com/' + self.gameName + '/currentStatus')
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req)
        data = json.load(response)
        return (self.coordConvertToTup(data['lastMove']), data['currentPlayer']) # gets tuple coordinates and current player from server

    def coordConvertToTup(self, coord): # covert the sring coordinates to a tuple
        return (int(coord[0]),int(coord[1]))

    def coordConvertToStr(self, coord): # convert the tuple coordinates to a string
        return str(coord[0]) + str(coord[1])

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
        print 'pieces' + str(pieces)
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
            self.sendMoveToServer(space)
            self.board[space] = self.player
            return True
        return False

    def sendMoveToServer(self,space):
        data = {
                'playerColor': self.playerColor,
                'move' : self.coordConvertToStr(space)
        }

        req = urllib2.Request('http://othello.herokuapp.com/' + str(self.gameName) + '/makeMove')
        req.add_header('Content-Type', 'application/json')

        response = urllib2.urlopen(req, json.dumps(data))

    def waitForUpdate(self,space):
        while(True):
            time.sleep(1)
            print 'wait'
            status = self.getCurrentStatus()
            if status[1] == self.playerColor and space != status[0]:
                self.updateFromServer()
                self.grid.makeBoard()
                return


    def updateBoard(self,coordinate):
        print 'self.player' + self.playerColor
        print 'self.player' + self.player
        if self.playerColor == self.player:
            self.checkDirect(self.player,coordinate)
            valid = self.fill_event(coordinate)
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
            return valid

if __name__ == "__main__":
    root = Tk()
    gui = Board(root)
    root.mainloop()
