# -*- coding: utf-8 -*-
from Tkinter import *
 
class Canvassing():
  def __init__(self, parent = None):
    self.canvas = Canvas(width=256, height=256, bg = "dark green")
    self.canvas.pack()
    for n in range(8):
    	self.canvas.create_line(1,32*n,256,32*n, fill = "green")
    for n in range(8):
    	self.canvas.create_line(32*n,1,32*n,256, fill = "green")
 
Canvassing()
mainloop()