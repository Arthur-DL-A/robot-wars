import importlib

class Board:
    def isPositionLegal(self, position):
        return self.data[position[1]][position[0]][1]
    
    def printBoard(self):
        for line in self.data:
            for tile in line:
                print(tile[0] + " ", end="")
            print()
    def loadFile(self, fileName):
        lines = open(fileName).readlines()
        tileDict = {}
        size = [int (i) for i in lines[0].split("x")]
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
     
    def __init__(self, dataFileName, players):
        '''
        The data structure in the format
        ("display-character", "traversable", "damageOnTraverse")
        '''
        self.data = []
        self.loadFile(dataFileName) 
        self.printBoard()
class PlayerWrapper:
    def __init__(self, playerRobot, initalPosition):
        self.playerRobot = playerRobot
        self.position = initialPosition
        self.health = 20
        self.energy = 4 #currently used for testing complex patterns
    
    def act(self, tiles, boardSize):
        attrDict = {
                "health":self.health,
                "energy":self.energy,
                "tiles": tiles,
                "boardsize": boardSize,
                "position": self.position
                }
        return self.playerRobot.act(attrDict)

def player_wait(player, direction):
    pass
def player_move(player, direction):
    if direction.strip() == "up":
        player.position = (player.position[0], player.position[1] - 1) # inverted due to stupid printing
    if direction.strip() == "down":
        player.position = (player.position[0], player.position[1] + 1) # same
    if direction.strip() == "left":
        player.position = (player.position[0] - 1, player.position[1])
    if direction.strip() == "right":
        player.position = (player.position[0] + 1, player.position[1])
def player_attack(player, direction):
    pass
def player_shoot(player, direction):
    pass
def makePlayerMove(player, move, direction):
    move_table = {
            "wait":(0, player_wait),
            "move":(1, player_move),
            "shoot":(2, player_attack),
            "attack":(1, player_shoot),
            }
    if(player.energy >= move_table[0]):
        player.energy()
        jump_table[move](player, direction)

def parsePlayerMove(player, moveString):
    moveTokens = moveString.split()
    currentToken = 0
    while currentToken < len(moveTokens):
        move = moveTokens[currentToken]
        direction = moveTokens[currentToken + 1]
        makePlayerMove(player, move, direction)
        currentToken += 2


player_one_module = importlib.import_module("ai-coward")
player_one_robot = player_one_module.Robot()
player_one = PlayerWrapper(player_one_robot)

player_two_module = importlib.import_module("ai-coward")
player_two_robot = player_two_module.Robot()
player_two = PlayerWrapper(player_two_robot)

board = Board("board.lvl")

number_of_turns = 100


