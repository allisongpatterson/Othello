# Create players and pieces
#EMPTY, BLACK, WHITE, EDGE = ('_','B','W','e')
#PIECES = (EMPTY, BLACK, WHITE, EDGE)
#PLAYERS = {BLACK: 'Black' , WHITE: 'White'}

#UP, DOWN, LEFT, RIGHT = (-10, 10, -1, 1)

#def print_board(board):
	#rep = ''
	#rep += 
def labels():
	print '    A   B   C   D   E   F   G   H'

def top_line(n):
	print '  +',
	print '- + ' * n

#top_line(8)
def pipes(n):
	for i in range(n):
		print ('|  '),
	print '|',

def board(n):
	labels()
	for i in range(n):
		top_line(n)
		print i+1,
		pipes(n)
		print '\n',
	top_line(n)

board(8)
