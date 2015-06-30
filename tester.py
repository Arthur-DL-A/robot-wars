#!/usr/bin/env python3
#
# The Robot Wars arena director.
#

import sys
import importlib

import attr_dict

class Board:
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
        attributes = {
                "health":self.health,
                "action_points":self.energy,
                "visible_tiles": tiles,
                "board_size": board_size,
                "location": self.position
                }
        return self.player_robot.act(attributes)

def player_wait(player, direction, board, players):
    pass

def player_move(player, direction, board, players):
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

def player_attack(player, direction, board, players):
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

def player_shoot(player, direction, board, players):
    pass

def make_player_move(player, board, move, direction, players):
    move_table = {
            "wait": (0, player_wait),
            "move": (1, player_move),
            "shoot": (2, player_attack),
            "attack": (1, player_shoot),
            }
    if(player.energy >= move_table[move][0]):
        player.energy -= move_table[move][0]
        move_table[move][1](player, direction, board, players)

def parse_player_move(player, board, moveString, players):
    player.energy = 4
    moveTokens = moveString.split()
    currentToken = 0
    while currentToken < len(moveTokens):
        move = moveTokens[currentToken]
        direction = moveTokens[currentToken + 1]
        make_player_move(player, board, move, direction, players)
        currentToken += 2



print(sys.argv)

#board = Board(sys.argv[1])

player_one_module = importlib.import_module(sys.argv[2])
player_one_robot = player_one_module.Robot()
player_one = PlayerWrapper(player_one_robot, (int(sys.argv[3]), int(sys.argv[4])))

player_two_module = importlib.import_module(sys.argv[5])
player_two_robot = player_two_module.Robot()
player_two = PlayerWrapper(player_two_robot, (int(sys.argv[6]), int(sys.argv[7])))


number_of_turns = 20

while number_of_turns > 0:
    board.print_board([player_one, player_two])
    parse_player_move(player_one, board, player_one.act(board.get_tiles(player_one.position, 3), board.board_size),[player_one, player_two])
    parse_player_move(player_two, board, player_two.act(board.get_tiles(player_one.position, 3), board.board_size), [player_one, player_two])
    number_of_turns -= 1

test_dict = AttrDict()
