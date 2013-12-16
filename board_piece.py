# class Board(object):
#     def __init__(self):
#         self.newboard = None
#         self.board = {}
#         for i in range(8):
#             for k in range (8):
#                 coord = str(k)  + str(i)
#                 self.board[tuple(coord)] = 'E'
#         self.place_piece_at('W', '3', '4')
#         self.place_piece_at('B', '3', '3')
#         self.place_piece_at('W', '4', '3')
#         self.place_piece_at('B', '4', '4')

#     def __str__(self):
#         for self.board[0] in range(8):
#             for self.board[1] in range(8):
#                 return str(self.board)


#     def place_piece_at(self, piece, x, y):
#         self.board[x,y] = piece



class Gameplay(object):
    '''Defines legal movements for pieces'''

 

    def __init__(self):
        self.board = {}
        for i in range(8):
            for k in range (8):
                coord = str(k)  + str(i)
                self.board[tuple(coord)] = 'E'
        self.board[('3','4')]='W'
        self.place_piece_at('W', '3', '4')
        self.place_piece_at('B', '3', '3')
        self.place_piece_at('W', '4', '3')
        self.place_piece_at('B', '4', '4')

    def place_piece_at(self, piece, x, y):
        self.board[x,y] = piece

    def switch_player(self,last_player):
        if last_player == 'B':
            player = 'W'
        else:
            player = 'B'
        return player

    def direct1(self,player,space):
        '''checks diagonal positive positive (northeast): x+1, y+1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]+i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]+i)] == player:
                    if self.board[str(space[0]+(i-1)),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.board[str(space[0]),str(space[1])] = player
        else:
            self.empty_space(space)
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct2(self,player,space):
        '''checks upward(north): x+0, y+1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]+i)] = 'C'
                if self.board[str(space[0]),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]+i)] == player:
                    if self.board[str(space[0]),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct3(self,player,space):
        '''checks diagonal negative positive (northwest): x-1, y+1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]-i),str(space[1]+i)] == oppcolor:
                    self.board[str(space[0]-i),str(space[1]+i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]+i)] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1]+i)] == player:
                    if self.board[str(space[0]-(i-1)),str(space[1]+(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct4(self,player,space):
        '''checks left(west): x-1, y+0'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]-i),str(space[1])] == oppcolor:
                    self.board[str(space[0]-i),str(space[1])] = 'C'
                if self.board[str(space[0]-i),str(space[1])] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1])] == player:
                    if self.board[str(space[0]-(i-1)),str(space[1])] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct5(self,player,space):
        '''checks diagonal negative negative (southwest): x-1, y-1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]-i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]-i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]-i),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]-i),str(space[1]-i)] == player:
                    if self.board[str(space[0]-(i-1)),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct6(self,player,space):
        '''checks downward (south): x+0, y-1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]),str(space[1]-i)] = 'C'
                if self.board[str(space[0]),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]),str(space[1]-i)] == player:
                    if self.board[str(space[0]),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct7(self,player,space):
        '''checks diagonal positive negative (southeast): x+1, y-1'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]+i),str(space[1]-i)] == oppcolor:
                    self.board[str(space[0]+i),str(space[1]-i)] = 'C'
                if self.board[str(space[0]+i),str(space[1]-i)] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1]-i)] == player:
                    if self.board[str(space[0]+(i-1)),str(space[1]-(i-1))] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def direct8(self,player,space):
        '''checks right (east): x+1, y+0'''
        if player == 'B':
            oppcolor = 'W'
        else:
            oppcolor = 'B'
        if self.board[str(space[0]),str(space[1])] == 'E':
            for i in range(1,8):
                if self.board[str(space[0]+i),str(space[1])] == oppcolor:
                    self.board[str(space[0]+i),str(space[1])] = 'C'
                if self.board[str(space[0]+i),str(space[1])] == 'E':
                    break 
                if self.board[str(space[0]+i),str(space[1])] == player:
                    if self.board[str(space[0]+(i-1)),str(space[1])] == 'C':
                        for key, value in self.board.items():
                            if value == 'C':
                                self.board[key] = player
                                self.switch_player(player)
                                self.board[str(space[0]),str(space[1])] = player
        for value in self.board:
            if value == 'C':
                value = oppcolor
        return self.board

    def empty_space(self,space):
        if self.board[str(space[0]),str(space[1])] == 'E':
            pass
        else:
            return 'Sorry, that is not a valid move! Please select an empty space.'

    def __str__(self):
        return str(self.board)

if __name__ == "__main__":

    # test_piece = Piece('B')
    # test_piece.flip()
    # print test_piece

    # test_board = Board()
    # print test_board

    test_game = Gameplay()
    coordinate = (2,2)
    piece_color = 'B'
    test_game.direct1(piece_color,coordinate)
    test_game.direct2(piece_color,coordinate)
    test_game.direct3(piece_color,coordinate)
    test_game.direct4(piece_color,coordinate)
    test_game.direct5(piece_color,coordinate)
    test_game.direct6(piece_color,coordinate)
    test_game.direct7(piece_color,coordinate)
    test_game.direct8(piece_color,coordinate)
    print test_game.turn_number
    # print test_game.board[('3','3')]



