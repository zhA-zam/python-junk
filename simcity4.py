'''
The values of pieces of land from the game Sim City are displayed in the position
of their corresponding land piece, with some of the values missing. Then the values
of pieces of land are displayed in the same manner but with the missing values 
replaced with an estimate of the value of the land piece. The stats of this information,
the average of all the land values and the highest of each, are also displayed.

The code for the user-defined functions create_grid(), display_grid(), and 
find_neighbor_values() was written with the assistance of the lecture slide 
titled 'CMPUT 174 - Multidimensional Lists'.
The code for finding the index of the missing values of the grid, in the
user-defined function fill_gaps(), was taken from the website Statistics Globe
at this link: https://statisticsglobe.com/find-index-element-nested-list-python

By: Zoha Azam
Date: Nov. 9, 2023
'''
from copy import deepcopy
import math

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    with open(filename, 'r') as file:
        alist = file.readlines()
    rows = int(alist[0].strip())
    cols = int(alist[1].strip())
    matrix = []
    index = 2
    for row_index in range(rows):
        a_row = []
        for col_index in range(cols):
            item = int(alist[index].strip())
            index = index + 1
            a_row.append(item)
        matrix.append(a_row)
    return matrix

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    for row in grid:
        a_row = ''
        for col in row:
            a_row = f'{a_row}{col:9}' 
        print(a_row)
        
def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    neighbours = []
    rows = len(grid) 
    cols = len(grid[0])
    for row_index in range(row-1,row+2):
        for col_index in range(col-1,col+2):
            if row_index < 0 or col_index < 0 or row_index >= rows or col_index >= cols:
                continue
            if row_index == row and col_index == col:
                continue        
            neighbours.append(grid[row_index][col_index])
    return neighbours         

def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid that is a copy of the original grid
    Call find_neighbor_values function to find the neighbors of each cell.
    Find the average of their values and round it to the nearest integer 
    Use the average values to fill in the missing values in the new grid.
    Return the new grid   
    """
    grid_copy = deepcopy(grid)
    missing_values = any(0 in values for values in grid_copy)
    if missing_values:  # if statement runs as long as 0 is an element in grid_copy        
        # Makes a nested list of the indices of any 0 in grid_copy
        zeroes = []      
        for i in range(len(grid_copy)):
            for j in range(len(grid_copy[i])):
                if grid_copy[i][j] == 0:
                    zeroes.append([i,j])  
                    
        for index in zeroes:
            # Finds the row index and column index of any 0 in grid_copy
            # to be used for find_neighbor_values()
            row = index[0]
            col = index[1]
            neighbours = find_neighbor_values(grid_copy, row, col)
            # The list stored in the identifier neighbours is used to
            # estimate the value that should replace any 0 in grid_copy
            neighbours_sum = 0
            for k in neighbours:
                neighbours_sum = neighbours_sum + k
            average = round((neighbours_sum/len(neighbours)))
            grid_copy[row][col] = average
    return grid_copy

def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    rows = len(grid)
    cols = len(grid[0])    
    # Makes a list of all of the land values
    land_values = []
    for i in range(rows):
        for j in range(cols):
            land_values.append(grid[i][j])            
    # Considers each element in the list of land values and as
    # long as an element is greater than the value defined as
    # max_value, then max_value becomes the value of that element            
    max_value = 0
    for value in land_values:
        if value > max_value:
            max_value = value
    return max_value

def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """ 
    rows = len(grid)
    cols = len(grid[0])    
    # Makes a list of all of the land values
    land_values = []
    for i in range(rows):
        for j in range(cols):
            land_values.append(grid[i][j])
    
    sum_of_values = 0
    for value in land_values:
        sum_of_values = sum_of_values + value
    average = round(sum_of_values/len(land_values))
    return average
    
def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated SimCity land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    average = find_average(new_grid)
    print(f"Average land value in this city: {average}")
    max_ = find_max(new_grid)
    print(f"Maximum land value in this city: {max_}")
    
if __name__ == '__main__':
    main()  # Runs the program