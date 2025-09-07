'''
Name: Zoha Azam
Date: Nov 22, 2023
'''
MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    # TODO: implement this function
    with open(map_file, 'r') as file:
        alist = file.readlines()
        
    for line in alist:
        line = line.strip()
    rows = len(alist)
    cols = len(line)
    grid = []
    for row_index in range(rows):
        a_row = []
        for col_index in range(cols):
            item = (alist[row_index][col_index])
            a_row.append(item)
        grid.append(a_row)
    return grid    

def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    # TODO: implement this function
    start = []      
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start.append([i,j]) 
    return start[0]

def get_command() -> str:
    """
    Gets a command from the user.
    """
    # TODO: implement this function
    command = input('> ')
    return command

def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    # TODO: implement this function
    row = player_position[0]
    col = player_position[1]
    grid[row][col] = '@'
    
    for row in grid:
        a_row = ''
        for col in row:
            a_row = f'{a_row}{col}'
        print(a_row)
               
def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    # TODO: implement this function
    grid_size = []
    grid_size.append(len(grid))
    grid_size.append(len(grid[0]))
    return grid_size

def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    # TODO: implement the rest of the function
    if position[0] >= 0 and position[0] < grid_rows and position[1] >= 0 and position[1] < grid_cols:
        return True
    else:
        return False    

def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:  
    """
    Returns the allowed directions.
    """
    grid_rows, grid_cols = get_grid_size(grid)
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if grid[row][col] != 'F':
        i = 0
        if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
            directions.append('north')
        elif 'north' in directions and grid[row - 1][col] not in allowed_objects:
            directions.pop(i)
        # TODO: implement the rest of the function
        if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
            directions.append('south')
        elif 'south' in directions and grid[row + 1][col] not in allowed_objects:
            directions.pop(i)            
        if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
            directions.append('east')
        elif 'east' in directions and grid[row][col + 1] not in allowed_objects:
            directions.pop(i)        
        if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
            directions.append('west')
        elif 'west' in directions and grid[row][col - 1] not in allowed_objects:
            directions.pop(i)        
        i = i + 1   
             
    return directions

def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    # TODO: implement this function
    directions = look_around(grid, grid_start)
    if direction in directions: 
        print("You can go north")    

def main():
    """
    Main entry point for the game.
    """
    # TODO: implement the main() function
    # TODO: update the main() function
    grid = load_map(MAP_FILE)
    grid_start = find_start(grid)
    
    directions = look_around(grid, [0,0])
    direction = ', '.join(directions)
    print(f'You can go {direction}')
    command = get_command().lower()
    success = move('west', position, grid)
    while command != 'escape':
        while command == 'show map':
            display_map(grid, grid_start)
            # look_around(grid, grid_start)
            print(f'You can go {direction}')             
            command = get_command().lower()
        if command != 'escape':
            print("I do not understand")
            # look_around(grid, grid_start)
            print(f'You can go {direction}')            
            command = get_command().lower()
           
if __name__ == '__main__':
    main()