'''
By: Zoha Azam
Date: Nov. 8, 2023
'''

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # TODO: Implement this function
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
    # TODO: Implement this function
    for row in grid:
        a_row = ''
        for col in row:
            a_row = f'{a_row}{col:9}' # IMPORTANT
        print(a_row)
        
def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    # TODO: Implement this function
    pass        

def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_1.txt")
    print("SimCity Land Values:")
    display_grid(grid)
    
if __name__ == '__main__':
    main()