from Tkinter import *

# player constants
player_names = ('', 'Black', 'White')
player_colors = ('', '#000000', '#ffffff') # black, white

class BoardState():
	def __init__(self, boardstate = None):
		if boardstate:
			# copy existing
			self._pieces = boardstate._pieces.copy()
			self._open = boardstate._open.copy()
			self._player = boardstate._player
			self._passed = boardstate._passed
		else:
			# create new board
			self._pieces = {(3,3):1, (3,4):2, (4,3):1, (4,4):2}
			# open spaces next to occupied spaces
			self._open = {(2,2):1,(2,3):1,(2,4):1,(2,5):1,
                          (3,2):1,                (3,5):1,
                          (4,2):1,                (4,5):1,
                          (5,2):1,(5,3):1,(5,4):1,(5,5):1}
        	self._player = 1 # black goes first
        	pelf._passed = 0 # used for game over
        def getPlayer(self):
        	# returns player whose turn it is
        	return self._player
        def getPieces(self):
        	# returns all current pieces as a dictionary: pieces[x,y] = player
        	return self._pieces
        def getMoves(self):
        	# returns list of valid moves and resulting boardstates (x,y,newBoardState)
        	# if only legal move is pass, x=y=None
        	# if no legal moves, empty list and game over
        	result = []
        	# find legal moves
        	for x,y in self._open.keys():
        		boardState = self._placePiece(x, y)
        		if boardState:
        			result.append((x, y, boardState))
        	if not result:
        		# no legal moves found
        		if self._passed:
        			return () # game over
        		boardState = BoardState(self)
        		boardState._passed = 1
        		boardState._changePlayers()
        		result.append ((None, None, boardState))
        	return result
        	# remove space of move from open space list
        	del newboard._open[x,y]
        	# add new open spaces surrounding new pieces
        def _placePiece(self, x, y):
        	

        	###########################################################


class Board():
	class Square:
		def __init__(self, x, y):
			self.x, self.y = x, y
			self.player = 0
			self.squareId = 0
			self.pieceId = 0

	def __init__(self, parent = None):
		# create frame for GUI
		self._frame = Frame()
		# set window title
		self._frame.master.wm_title('Othello')
		self._canvas = Canvas(self._frame, width=256, height=256, bg = '#008000') # med green
		self._canvas.pack()
		# make start button
		self._menuFrame = Frame(self._frame)
		self._menuFrame.pack(expand = Y, fill = X)
		self._newGameButton = Button(self._menuFrame, text = 'Hello World', command = self._newGame)
		self._newGameButton.pack(side = LEFT, padx = 5)
		Label(self._menuFrame).pack(side = LEFT, expand = Y, fill = X)

	def play(self):
		'Play the game!'
		self._frame.mainloop()

	def _newGame(self):
		# delete pieces
		for s in self._squares.values():
			if s.pieceId:
				self._canvas.delete(s.pieceId)
				s.pieceId = 0
		# create new board
		self._state = Board()
		self.updateBoard()

#Board()
#mainloop()

if __name__ == '__main__':
	board = Board()
	board.play()