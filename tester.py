import importlib

class PlayerWrapper:
    def __init__(self, playerRobot):
        self.playerRobot = playerRobot
        self.health = 20
        self.energy = 4 #currently used for testing complex patterns
    
    def act(self, tiles, boardSize, position):
        attrDict = {
                "health":self.health,
                "energy":self.energy,
                "tiles": tiles,
                "boardsize": boardSize,
                "position": position
                }
        return self.playerRobot.act(attrDict)


player_one_module = importlib.import_module("ai-coward")
player_one_robot = player_one_module.Robot()
player_one = PlayerWrapper(player_one_robot)
print(player_one.act([],(0,0), (0,0)))

number_of_turns = 100


