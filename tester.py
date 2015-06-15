import importlib

class ServerModuleWrapper:
    def __init__(self, playerModule):
        self.playerModule = playerModule
        self.health = 20
        self.energy = 4 #currently used for testing complex patterns
    
    def react(position):
        pass


player_one_module = importlib.import_module("player1")
player_two_module = importlib.import_module("player2")

number_of_turns = 100


