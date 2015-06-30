#!/usr/bin/env python3
#
# The Robot Wars arena director.
#

import sys
import importlib

import attr_dict.AttrDict as struct

class BoardPlayerManager:
    '''
    A class that manages the board and its players and runs the high level logic of the game
    '''
    def __init__ (self, board, players):
        ''' Takes the board and players as input and returns an int giving the index of the player that won '''
        self.board = board
        self.players = players
        while not 0 in map(lambda player: player.health, players):# while none of the players healths are 0
            #play the game
            for player in players:
                self.make_player_move(player, player.act(self.board.get_tiles(player.position,3)))
                # Hard coding a value of 3 for the sight range 
                        

    def player_wait(self):
        pass

    def player_move(self):
        dest = ()
        if direction.strip() == "up":
            dest = (player.position[0], player.position[1] - 1) # inverted due to stupid printing
        if direction.strip() == "down":
            dest = (player.position[0], player.position[1] + 1) # same
        if direction.strip() == "left":
            dest = (player.position[0] - 1, player.position[1])
        if direction.strip() == "right":
            dest = (player.position[0] + 1, player.position[1])

        if board.data[dest[1]][dest[0]][1]:
            player.position = dest

    def player_attack(self):
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

    def player_shoot(self):
        pass

    def make_player_move(self, player, player_move_list):
        for move in player_move_list:
            move_type = move[0]
            move_direction = move[1] # is this a fair assumption?
            move_table = {
                    "wait": (0, self.player_wait),
                    "move": (1, self.player_move),
                    "shoot": (2, self.player_attack),
                    "attack": (1, self.player_shoot),
                    }
            if player.energy >= move_table[move][0]:
                player.energy -= move_table[move][0]
                move_table[move][1](player, move_direction, self.board,
                                    self.players)

    
class Board:
    ''' 
    A class that loads a board file and allows you to perform operations on the loaded data
    '''
    def get_tiles(self, position, size):
        return self.data[position[1]-size:position[1]+size][position[0]-size:position[0]+size]

    def print_board(self, players):
        current_line = 0
        current_tile = 0
        for line in self.data:
            for tile in line:
                printed = False
                for player in players:
                    if player.position == (current_tile, current_line):
                        print("@ ", end="")
                        printed = True
                if not printed:
                    print(tile[0] + " ", end="")
                    printed = True
                current_tile +=1
            current_tile = 0
            current_line += 1
            print()

    def load_file(self, filename):
        lines = open(filename).readlines()
        tile_dict = {}
        size = [int (i) for i in lines[0].split("x")]
        self.board_size = size
        lines = lines[1:]
        skipcount = 0
        for line in lines:
            skipcount += 1
            if(line.strip() == "endtiles"):
                break
            disp_char, traversable, damage_on_traverse = line.split()
            tile_dict[disp_char] = (disp_char, traversable.strip() == "y", int(damage_on_traverse))
        print (skipcount)
        lines = lines[skipcount:]
        for line in lines:
            tileList = []
            for char in line.strip():
                tileList.append(tile_dict[char])
            self.data.append(tileList)

    def __init__(self, dataFileName):
        '''
        The data structure in the format
        ("display-character", "traversable", "damage_on_traverse")
        '''
        self.data = []
        self.board_size = (0,0)
        self.load_file(dataFileName)
        self.print_board([])

class PlayerWrapper:
    def __init__(self, player_robot, initial_position):
        self.player_robot = player_robot
        self.position = initial_position
        self.health = 20
        self.energy = 4 #currently used for testing complex patterns

    def act(self, tiles, board_size):
        attributes = struct(**{
                "health":self.health,
                "action_points":self.energy,
                "visible_tiles": tiles,
                "board_size": board_size,
                "location": self.position
                })
        return self.player_robot.act(attributes)

if __name__ == "__main__":
    pass
