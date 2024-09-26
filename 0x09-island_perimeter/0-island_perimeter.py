#!/usr/bin/python3
""" 0. Island Perimeter
Contains a function island_perimeter(grid) that returns the
perimeter of the island described in grid.
"""


def island_perimeter(grid):
    """Calculate island perimeter

    Argument:
    - grid: is a list of list of integers

    Return:
    - the perimeter of the island described in grid
    """
    land_perimeter = 0  # initialize the total land perimeter in grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            j_perimeter = 0  # initialize grid cell perimeter
            if grid[i][j] == 1:  # check if cell is land = 1
                j_perimeter = 4
                # check for connection to adjacent cells
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    j_perimeter -= 1
                if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                    j_perimeter -= 1
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    j_perimeter -= 1
                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    j_perimeter -= 1

            land_perimeter += j_perimeter

    return land_perimeter
