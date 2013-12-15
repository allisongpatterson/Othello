from Tkinter import*

class Board(Canvas):
    global scaling_factor
    scaling_factor=90
    
    def __init__(self, parent):
        Canvas.__init__(self, parent, background='forest green')    
        
        self.parent = parent
        self.parent.title("Othello")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.drawGrid()
        self.bind("<1>", self.Move)

    def centerWindow(self):
        self.w = scaling_factor*8
        self.h = scaling_factor*8

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw - self.w)/2
        y = (sh - self.h)/2
        self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))

    def drawGrid(self):
        #horizontal lines
        for n in range(1,9):
            self.create_line(0,scaling_factor*n,self.w,scaling_factor*n, fill = 'black', width=5)
        #vertical lines
        for n in range(1,9):
            self.create_line(scaling_factor*n,0,scaling_factor*n,self.w, fill = 'black',width=5)

    def Move(self, event):
        #print "frame coordinates: %s,%s" % (event.x, event.y)
        x=(int(event.x/scaling_factor)*scaling_factor)+(scaling_factor/2)
        y=(int(event.y/scaling_factor)*scaling_factor)+(scaling_factor/2)
        r=scaling_factor/4
        self.create_oval(x-r,y-r,x+r,y+r,fill='black',outline='black')
        return (int(event.x/scaling_factor)+1,int(event.y/scaling_factor)+1)    #returns coordinate that goes into logic

def main():
    root = Tk()
    Board(root)
    root.mainloop()  

if __name__ == '__main__':
    main()  