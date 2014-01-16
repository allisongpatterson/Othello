from swampy.Gui import * 
import os

class Gwindow(): 
	def __init__(self):
		self.g = Gui() # make g window
		self.g.title('Othello!')
		self.g.gr(cols=2)
		localButton = self.g.bu(text='Local Game', command=self.local)
		internetButton = self.g.bu(text='Internet Game', command=self.internet)
		self.g.mainloop()

	def local(self):
		self.g.destroy() # close g window
		os.system('python board_piece_final_tweaked.py') # start local game

	def internet(self):
		self.g.destroy() # close g window
		Hwindow()


class Hwindow():
	def __init__(self):
		self.h = Gui() # make h window
		self.h.title('Othello!')
		self.entryField = self.h.en(text='Game name...')
		self.h.gr(cols=2)
		hostButton = self.h.bu(text='Host Game', command=self.host)
		joinButton = self.h.bu(text='Join Game',command=self.join)
		self.h.mainloop()
	def host(self):
		self.h.destroy() # close h window
		print self.entryField.get()

	def join(self):
		self.h.destroy() # close h window

if __name__ == "__main__":
    Gwindow()