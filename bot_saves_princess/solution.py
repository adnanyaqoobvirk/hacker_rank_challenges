#!/usr/bin/python

def get_positions(grid):
    bot_position = None
    princess_position = None
    
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == 'm':
                bot_position = (i, j)
            elif char == 'p':
                princess_position = (i, j)
    return bot_position, princess_position

def display_path_to_princess(grid):
    bot_position, princess_position = get_positions(grid)
    vertical_move_count = bot_position[0] - princess_position[0]
    horizontal_move_count = bot_position[1] - princess_position[1]
    
    vertical_movement = "UP" if vertical_move_count >= 0 else "DOWN"
    horizontal_movement =  "LEFT" if horizontal_move_count >= 0 else "RIGHT"

    for _ in range(abs(vertical_move_count)):
        print(vertical_movement)
    
    for _ in range(abs(horizontal_move_count)):
        print(horizontal_movement)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

display_path_to_princess(grid)