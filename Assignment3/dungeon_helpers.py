deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dir_words = ["east", "west", "south", "north"]

def get_directions(dungeon_map, coord):
    x, y = coord
    dirs = []
    for delta, word in zip(deltas, dir_words):
        dx, dy = delta
        if dungeon_map[x+dx][y+dy] != 'x':
            dirs.append(word)
    return dirs

def get_directions_message(dungeon_map, coord):
    dirs = get_directions(dungeon_map, coord)
    return "There is a door to your " + ", ".join(dirs) + "\n" + get_warning_message(dungeon_map, coord)

def get_next_coordinate(coord, dir_word):
    delta = deltas[dir_words.index(dir_word.lower())]
    return (coord[0]+delta[0], coord[1]+delta[1])

def get_warning_message(dungeon_map, coord):
    messages = ""
    neighboring_coords = [get_next_coordinate(coord, word) for word in dir_words]
    for neighbor in neighboring_coords:
        x, y = neighbor
        char = dungeon_map[x][y]
        
        if char == '^':
            messages += "You feel frightened for a moment, as if a trap is nearby.\n"
        elif char == 'T':
            messages += "You feel like your luck might be picking up.\n"
    
    return messages