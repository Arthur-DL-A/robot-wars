
class BoardPlayerManager:
    '''
    A class that manages the board and its players and runs the high level logic of the game
    '''
    def __init__ (self, board, players, maxTurns):
        ''' Takes the board and players as input and returns an int giving the index of the player that won '''
        self.board = board
        self.players = players
        for i in range(maxTurns):
            # print turn details
            print ("\n\nTurn number", i, ":") 
            #play the game
            if 0 in map(lambda player: player.health, players):# while none of the players healths are 0
                break # End the game
            self.board.print_board(self.players)
            for player in players:
                self.make_player_move(player, player.act(self.board.get_tiles(player.position,3), self.board.board_size))
                # Hard coding a value of 3 for the sight range 
        for player in players:
            print (player.display_chr,":", player.health)
            

    def player_guard(self, player, move_data, board, players):
        ''' 
        ok, this is a test idea for guard.
        is it alright for a place to start?
        '''
        player.health += 1

    def player_move(self, player, move_data, board, players):
        direction = move_data[0]
        dest = ()
        # check the destination tile
        if direction.strip() == "up":
            dest = (player.position[0], player.position[1] - 1) # inverted due to stupid printing
        if direction.strip() == "down":
            dest = (player.position[0], player.position[1] + 1) # same
        if direction.strip() == "left":
            dest = (player.position[0] - 1, player.position[1])
        if direction.strip() == "right":
            dest = (player.position[0] + 1, player.position[1])

        if board.data[dest[1]][dest[0]][1]:# if the board tile is traversable
            player.position = dest # move there

    def player_attack(self, player, move_data, board, players):
        direction = move_data[0]
        for other_player in players:
            if direction.strip() == "up":
                if other_player.position == (player.position[0] - 1, player.position[1]):
                    other_player.health -= 1
            if direction.strip() == "down":
                if other_player.position == (player.position[0] + 1, player.position[1]):
                    other_player.health -= 1
            if direction.strip() == "left":
                if other_player.position == (player.position[0], player.position[1] - 1):
                    other_player.health -= 1
            if direction.strip() == "right":
                if other_player.position == (player.position[0], player.position[1] + 1):
                    other_player.health -= 1

    def player_shoot(self, player, move_data, board, players):
        pass

    def make_player_move(self, player, player_move_list):
        for move in player_move_list:
            move_type = move[0]
            move_data = move[1:]
            move_table = {
                    "guard": (0, self.player_guard),
                    "move": (1, self.player_move),
                    "shoot": (2, self.player_attack),
                    "attack": (1, self.player_shoot),
                    }
            if player.energy >= move_table[move_type][0]:
                player.energy -= move_table[move_type][0]
                move_table[move_type][1](player, move_data, self.board,
                                    self.players)
                '''except:
                    raise Exception ("You messed up somewhere 'cause you tried to call [" + move_type + "] with arguements " + str(move_data))'''

