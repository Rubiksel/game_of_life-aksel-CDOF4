##### IMPORTS #####

import random

##### FUNCTIONS #####

def get_neighbors(row, col, grid):
    neighbors = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i < 0 or i >= len(grid) or j < 0 j >= len(grid[0]):
                continue
            if not (i == row and j == col):
                neighbors.append((i, j))
    return neighbors

def update_cell(row, col, grid):
    live_neighbors=0
    for neighbor in get_neighbors(row, col, grid):
        r, c = neighbor
        if grid[r][c] == 1:
            live_neighbors += 1
    if grid[row][col] == 1:
        if live_neighbors < 2 or live_neighbors > 3:
            return 0
    else:
        if live_neighbors == 3:
            return 1
    return grid[row][col]

def next_gen(grid):
    new_grid = grid.copy()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid[i][j] = update_cell(i, j, grid)
    return new_grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

##### MAIN #####
        
grid = [[random.choice([0, 1]) for _ in range(20)] for _ in range(20)]
while True:
    print_grid(grid)
    grid = next_gen(grid)
    input("Press Enter to continue...")