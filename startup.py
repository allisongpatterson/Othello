from swampy.Gui import * 
import os
import json
import urllib2

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
		data = {
				'gameName': self.entryField.get()
		}

		req = urllib2.Request('http://othello.herokuapp.com/createGame')
		req.add_header('Content-Type', 'application/json')

		response = urllib2.urlopen(req, json.dumps(data))
		os.system('python board_piece_final_tweaked1.py ' + self.entryField.get() + ' black')
		self.h.destroy() # close h window

	def join(self):
		os.system('python board_piece_final_tweaked1.py ' + self.entryField.get() + ' white')
		self.h.destroy() # close h window

if __name__ == "__main__":
    Gwindow()