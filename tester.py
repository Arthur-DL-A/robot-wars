#!/usr/bin/env python3
#
# The Robot Wars arena director.
#

import sys
import importlib
from tester_module.Board import Board as Board
from tester_module.BoardPlayerManager import BoardPlayerManager as BoardPlayerManager
from tester_module.PlayerWrapper import PlayerWrapper as PlayerWrapper


    

def parse_player_line(player_line):
    '''
    returns the corresponding player object
    '''
    dummy, disp_chr, position_str, module_name = player_line.split() 
    # The dummy is there to make the file format work cleaner I could do some string parse but why?
    player_module = importlib.import_module(module_name)
    player_robot = player_module.Robot()
    useable_robot = PlayerWrapper(player_robot, disp_chr, tuple([int(pos) for pos in position_str.split("x")])) # Return the parsed player wrapper
    return useable_robot
def load_level(filename):
    '''
    This function returns the needed things in this format
    (Board, [players*])
    '''
    file_lines = [line.strip() for line in open(filename).readlines()]
    split_index = -1
    for line_index in range(len(file_lines)):
        if file_lines[line_index] == "endplayers":
            split_index = line_index
            break
    if split_index == -1:
        raise Exception ("No end player block found in the file")
    player_lines = file_lines[:split_index]
    board_lines = file_lines[split_index + 1:] # the +1 is to exclude the indicator line
    return Board(board_lines), [parse_player_line(player_line) for player_line in player_lines]


if __name__ == "__main__":
    board, players = load_level(sys.argv[1])
    manager = BoardPlayerManager(board, players, 10)

