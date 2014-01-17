from swampy.Gui import * 
import os
import json
import urllib2

class Gwindow(): 
	"""Creates local/internet menu."""
	def __init__(self):
		self.g = Gui() # make g window
		self.g.title('Othello!')
		self.g.gr(cols=2)
		localButton = self.g.bu(text='Local Game', command=self.local)
		internetButton = self.g.bu(text='Internet Game', command=self.internet)
		self.g.mainloop()

	def local(self):
		"""Creates a game w/ 2 players on 1 computer."""
		self.g.destroy() # close g window
		os.system('python board_piece_final_tweaked.py') # start local game

	def internet(self):
		"""Leads to next menu."""
		self.g.destroy() # close g window
		Hwindow()


class Hwindow():
	"""Creates host/join menu."""
	def __init__(self):
		self.h = Gui() # make h window
		self.h.title('Othello!')
		self.h.la(text='Game Name (no spaces)')
		self.entryField = self.h.en()
		self.h.gr(cols=2)
		hostButton = self.h.bu(text='Host Game', command=self.host)
		joinButton = self.h.bu(text='Join Game',command=self.join)
		self.h.mainloop()

	def host(self):
		"""Creates a game w/ 2 players and 2 computers."""
		name = self.entryField.get()
		data = {
				'gameName': name
		}

		req = urllib2.Request('http://othello.herokuapp.com/createGame')
		req.add_header('Content-Type', 'application/json')

		response = urllib2.urlopen(req, json.dumps(data))
		self.h.destroy() # close h window
		os.system('python board_piece_final_tweaked1.py ' + name + ' black')

	def join(self):
		"""Joins an existing game w/ 2 players and 2 computers."""

		name = self.entryField.get()
		self.h.destroy() # close h window
		os.system('python board_piece_final_tweaked1.py ' + name + ' white')
 
if __name__ == "__main__":
    Gwindow()