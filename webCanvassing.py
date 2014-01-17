from Tkinter import*
from webGameLogic import*
import time

class Board(Canvas):
    """Makes an 8 by 8 grid. Users can click anywhere on grid to place a 
    new piece. Uses a dictionary to determine what color the circles 
    should be.

    Gameplay(): Imported class that returns a dicitonary."""

    global scaling_factor

    scaling_factor=97

    def __init__(self, parent):

        Canvas.__init__(self, parent, background='forest green')    
        
        self.parent = parent
        self.pack(fill=BOTH, expand=1)     
        self.game=Gameplay(self)
        self.centerWindow()
        if self.game.player == 'black' and self.game.playerColor != 'black':
            self.parent.update_idletasks()
            self.game.waitForUpdate((4,4))
        self.bind("<1>", self.Move)        

    def centerWindow(self):
        """Centers the window."""

        self.w = scaling_factor*8
        self.h = scaling_factor*8

        self.sw = self.parent.winfo_screenwidth()
        self.sh = self.parent.winfo_screenheight()
        
        x = (self.sw - self.w)/2
        y = (self.sh - self.h)/2
        self.makeBoard()
        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))
     
    def makeBoard(self):
        """Makes a circle on the grid. Coordinate specified by dictionary key
        and color specified by dictionary value."""
        logic = self.game
        #horizontal lines
        for n in range(1,9):
            self.create_line(0,scaling_factor*n,self.w,scaling_factor*n, fill = 'black', width=5)
        #vertical lines
        for n in range(1,9):
            self.create_line(scaling_factor*n,0,scaling_factor*n,self.w, fill = 'black',width=5)
        self.r=scaling_factor/4
        for coordinates in logic.board:
            if logic.board[coordinates] == 'white' or logic.board[coordinates] == 'black':
                self.create_oval(int(coordinates[0])*scaling_factor+self.r,int(coordinates[1])*scaling_factor+self.r,(int(coordinates[0])+1)*scaling_factor-self.r,(int(coordinates[1])+1)*scaling_factor-self.r,fill=logic.board[coordinates],outline=logic.board[coordinates])
 
    def Move(self, event, point = None):
        """Scales coordinates from user's click for Gameplay."""
        if (event.x,event.y)<=(self.w,self.h):
            x=(int(event.x/scaling_factor)*scaling_factor)+(scaling_factor/2)
            y=(int(event.y/scaling_factor)*scaling_factor)+(scaling_factor/2)
            self.point = (int(event.x/scaling_factor)),(int(event.y/scaling_factor))
            valid = self.game.updateBoard(self.point)
            self.parent.update_idletasks()
            if valid:
                self.game.waitForUpdate((4,4))
            self.parent.update_idletasks()

  

def main():
    logic = Gameplay()

if __name__ == '__main__':
    main() 