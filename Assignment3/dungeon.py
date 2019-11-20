# Updated template November 10.

import random
from dungeon_helpers import get_directions, get_directions_message, get_next_coordinate

class Player():
    def __init__(self, name):
        # fill in here
        # 初始化实例属性
        self.name = name
        self.health = 10
    
    def get_name(self):
        # fill in here
        # 返回实例属性name
        return self.name
    
    def get_health(self):
        # fill in here
        return self.health
    
    def set_health(self, health):
        # fill in here
        try:
            # 判断health参数是否符合要求
            if not isinstance(health, int) or health >= 0:
                raise ValueError('ValueError: health must be integer, and great or equal to zero.')
        # 捕获异常，并输出异常信息
        except ValueError as e:
            print(e)
        self.health = health

class Dungeon():
    def __init__(self, map_filename, num_traps):
        # fill in here
        # 检查num_traps是否大于等于0，否则引发异常
        if num_traps < 0:
            raise ValueError('ValueError: num traps must be greater or equal zero.')
        # 调用方法，获取文件中地图
        self.dungeon_map = self.read_map_file(map_filename)
        #检查地图大小是否符合要求
        rows = len(self.dungeon_map)
        columns = len(self.dungeon_map[0])
        # 地图不是正方形
        if rows != columns:
            raise ValueError('ValueError: non-squregrid!')
        # 地图大小小于4
        if rows < 4:
            raise ValueError('ValueError: grid smaller than 4x4!')
        # 检查地图中是否包含非法字符
        letters = 'x*T'
        # 双重循环，逐个检查
        for row in self.dungeon_map:
            for char in row:
                # 有非法字符引发异常
                if char not in letters:
                    raise ValueError('ValueError: invalid characters in grid.')
        # 检查地图中是否存在Treasure
        flag = False #存在标志
        for row in self.dungeon_map:
            for char in row:
                if char == 'T':
                    flag = True
                    break
        # 地图中不存在Treasure，引发异常
        print(self.dungeon_map)
        if not flag:
            raise ValueError('ValueError: No treasure.')
        # 给属性num_traps赋值
        self.num_traps = num_traps
        # 调用加入trap的方法
        self.add_traps()
    
    def read_map_file(self, filename):
        # fill in here
        map_datas = []
        # 打开文件
        with open(filename, 'r') as f:
            # 逐行读取
            for line in f.readlines():
                # 删除换行符
                line = line.strip('\n')
                # 转为列表
                line = list(line)
                map_datas.append(line)
        return map_datas
    
    def get_coords_of_empty_spaces(self):
        # fill in here
        empty_spaces_coords = []
        # 双重循环遍历地图字符
        for i in range(len(self.dungeon_map)):
            for j in range(len(self.dungeon_map)):
                # 坐标处如果为empty spaces,则将坐标加入结果列表中
                if self.dungeon_map[i][j] == '*':
                    empty_spaces_coords.append((i, j))
        return empty_spaces_coords
    
    def get_char_at(self, coord):
        # fill in here
        try:
            # 返回指定字符
            return self.dungeon_map[coord[0]][coord[1]]
        # 捕获异常
        except IndexError as e:
            print(e)
    
    def visit_square(self, coord, player):
        # fill in here
        # 获取指定坐标处的字符
        char = self.get_char_at(coord)
        # 指定坐标处字符为T时，获取到treasure, The game is over.
        if char == 'T':
            print(player.get_name(), 'Get the Treasure!')
            print('The game is over.')
            return True
        # 指定坐标处字符为^，健康值-1
        if char == '^':
            player.set_health(player.get_health() - 1)
            # 玩家健康值为0时，The game is over.
            if player.get_health() == 0:
                # 打印输出信息
                print((player.get_name(), '\'s health is 0!'))
                print('The game is over.')
                return True
        return False

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