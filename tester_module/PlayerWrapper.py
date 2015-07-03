from attr_dict import AttrDict as struct

class PlayerWrapper:
    max_energy = 4
    def __init__(self, player_robot, display_chr, initial_position):
        self.player_robot = player_robot
        self.display_chr = display_chr
        self.position = initial_position
        self.health = 20
        self.energy = PlayerWrapper.max_energy #currently used for testing complex patterns

    def act(self, tiles, board_size):
        self.energy = PlayerWrapper.max_energy
        attributes = struct(**{
                "health":self.health,
                "action_points":self.energy,
                "visible_tiles": tiles,
                "board_size": board_size,
                "location": self.position
                })
        return self.player_robot.act(attributes)
