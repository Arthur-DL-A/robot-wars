
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
                        print(player.display_chr, "", end="")
                        printed = True
                if not printed:
                    print(tile[0] + " ", end="")
                    printed = True
                current_tile +=1
            current_tile = 0
            current_line += 1
            print()

    def load_file(self, file_lines):
        lines = file_lines
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

    def __init__(self, data_file_lines):
        '''
        The data structure in the format
        ("display-character", "traversable", "damage_on_traverse")
        '''
        self.data = []
        self.board_size = (0,0)
        self.load_file(data_file_lines)
        self.print_board([])

