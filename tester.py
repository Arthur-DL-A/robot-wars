import importlib
import sys

class Board:
    def getTiles(self, position, size):
        return self.data[position[1]-size:position[1]+size][position[0]-size:position[0]+size]

    def printBoard(self, players):
        currentLine = 0
        currentTile = 0
        for line in self.data:
            for tile in line:
                printed = False
                for player in players:
                    if player.position == (currentTile, currentLine):
                        print("@ ", end="")
                        printed = True
                if not printed:
                    print(tile[0] + " ", end="")
                    printed = True
                currentTile +=1
            currentTile = 0
            currentLine += 1
            print()
    def loadFile(self, fileName):
        lines = open(fileName).readlines()
        tileDict = {}
        size = [int (i) for i in lines[0].split("x")]
        self.boardSize = size
        lines = lines[1:]
        skipcount = 0
        for line in lines:
            skipcount += 1
            if(line.strip() == "endtiles"):
                break
            disp_char, taversable, damageOnTraverse = line.split()
            tileDict[disp_char] = (disp_char, taversable.strip() == "y", int(damageOnTraverse))
        print (skipcount)
        lines = lines[skipcount:]
        for line in lines:
            tileList = []
            for char in line.strip():
                tileList.append(tileDict[char])
            self.data.append(tileList)
     
    def __init__(self, dataFileName):
        '''
        The data structure in the format
        ("display-character", "traversable", "damageOnTraverse")
        '''
        self.data = []
        self.boardSize = (0,0)
        self.loadFile(dataFileName) 
        self.printBoard([])
class PlayerWrapper:
    def __init__(self, playerRobot, initialPosition):
        self.playerRobot = playerRobot
        self.position = initialPosition
        self.health = 20
        self.energy = 4 #currently used for testing complex patterns
    
    def act(self, tiles, boardSize):
        attrDict = {
                "health":self.health,
                "action_points":self.energy,
                "visible_tiles": tiles,
                "board_size": boardSize,
                "location": self.position
                }
        return self.playerRobot.act(attrDict)

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
def makePlayerMove(player, board, move, direction, players):
    move_table = {
            "wait":(0, player_wait),
            "move":(1, player_move),
            "shoot":(2, player_attack),
            "attack":(1, player_shoot),
            }
    if(player.energy >= move_table[move][0]):
        player.energy -= move_table[move][0]
        move_table[move][1](player, direction, board, players)

def parsePlayerMove(player, board, moveString, players):
    player.energy = 4
    moveTokens = moveString.split()
    currentToken = 0
    while currentToken < len(moveTokens):
        move = moveTokens[currentToken]
        direction = moveTokens[currentToken + 1]
        makePlayerMove(player, board, move, direction, players)
        currentToken += 2
print(sys.argv)

player_one_module = importlib.import_module(sys.argv[2])
player_one_robot = player_one_module.Robot()
player_one = PlayerWrapper(player_one_robot, (int(sys.argv[3]), int(sys.argv[4])))

player_two_module = importlib.import_module(sys.argv[5])
player_two_robot = player_two_module.Robot()
player_two = PlayerWrapper(player_two_robot, (int(sys.argv[6]), int(sys.argv[7])))

board = Board(sys.argv[1])

number_of_turns = 20

while number_of_turns > 0:
    board.printBoard([player_one, player_two])
    parsePlayerMove(player_one, board, player_one.act(board.getTiles(player_one.position, 3), board.boardSize),[player_one, player_two])
    parsePlayerMove(player_two, board, player_two.act(board.getTiles(player_one.position, 3), board.boardSize), [player_one, player_two])
    number_of_turns -= 1
