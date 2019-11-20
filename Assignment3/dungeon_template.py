# Updated template November 10.

import random
from dungeon_helpers import get_directions, get_directions_message, get_next_coordinate

class Player():
    def __init__(self, name):
        # fill in here
        pass # delete this line when you have written your code
    
    def get_name(self):
        # fill in here
        pass # delete this line when you have written your code
    
    def get_health(self):
        # fill in here
        pass # delete this line when you have written your code
    
    def set_health(self, health):
        # fill in here
        pass # delete this line when you have written your code

class Dungeon():
    def __init__(self, map_filename, num_traps):
        # fill in here
        pass # delete this line when you have written your code
    
    def read_map_file(self, filename):
        # fill in here
        pass # delete this line when you have written your code
    
    def get_coords_of_empty_spaces(self):
        # fill in here
        pass # delete this line when you have written your code
    
    def get_char_at(self, coord):
        # fill in here
        pass # delete this line when you have written your code
    
    def visit_square(self, coord, player):    
        # fill in here
        pass # delete this line when you have written your code
    
    def enter(self, player):
        cur_coord = self.get_starting_coordinate()
        num_moves = 0
        
        while True:
            game_over = self.visit_square(cur_coord, player)
            if game_over:
                break # end of game
            
            print(get_directions_message(self.dungeon_map, cur_coord))
            chosen_direction = input("Where would you like to go?\n>")
            valid_directions = get_directions(self.dungeon_map, cur_coord)
            if chosen_direction not in valid_directions:
                print("Invalid direction.")
                continue
            
            cur_coord = get_next_coordinate(cur_coord, chosen_direction)
            num_moves += 1
    
    def get_starting_coordinate(self):
        empty_spaces = self.get_coords_of_empty_spaces()
        return random.choice(empty_spaces)
    
    def add_traps(self):
        coords_of_empty_spaces = self.get_coords_of_empty_spaces()
        while self.num_traps > 0:
            coord = random.choice(coords_of_empty_spaces)
            self.dungeon_map[coord[0]][coord[1]] = '^'
            coords_of_empty_spaces.remove(coord)
            self.num_traps -= 1

name = input("Please enter player name:\n> ")
player = Player(name)
dungeon = Dungeon("d1.txt", 4)
dungeon.enter(player)