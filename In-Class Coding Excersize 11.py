# Multi-dimensional lists
# (Module 7)

'''

'''

# Nested 2D list:
matrix = [ [1, 2 ,3],
           [4, 5, 6],
           [7, 8, 9] ]

# Indexing requires matrix[row_index][col_index]
# Double subscription
print(matrix[0][0], matrix[0][1], matrix[0][2])
print(matrix[1][0], matrix[1][1], matrix[1][2])
print(matrix[2][0], matrix[2][1], matrix[2][2])

# for loops to create 2D lists
matrix = []
rows = 3
cols = 4
for i in range(rows):
    a_row = []
    for j in range(cols):
        a_row.append(j)
    matrix.append(a_row)
print(matrix)

# Printing a matrix (method 1)

matrix = [ [1, 2 ,3],
           [4, 5, 6],
           [7, 8, 9] ]
for row in matrix:
    a_row = ''
    for col in row:
        a_row += str(col) + '  '
    print(a_row)

# printing a matrix (method 2)
print("")
matrix = [ [1, 2 ,3],
           [4, 5, 6],
           [7, 8, 9] ]
num_rows = len(matrix)
num_columns = len(matrix[0])
for row_index in range(num_rows):
    a_row = ''
    for col_index in range(num_columns):
        a_row += str(matrix[row_index][col_index]) + '  '
    print(a_row)
    
'''
Coding Excersize
'''
print("")
# remember that first line is rows and second line is columns in the file
def build_matrix(filename):
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

def display_matrix_1(matrix):
    for row in matrix:
        a_row = ''
        for col in row:
            a_row = a_row + str(col) + '  '
        print(a_row)

def display_matrix_2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row_index in range(rows):
        a_row = ''
        for col_index in range(cols):
            a_row = a_row + str(matrix[row_index][col_index]) + '  '
        print(a_row)

def main():
    filename = 'matrix.txt'
    matrix = build_matrix(filename)
    print("Displaying the matrix by accessing the elements directly:")
    display_matrix_1(matrix)
    print("")
    print("Displaying the matrix by accessing the position of the elements:")
    display_matrix_2(matrix)
    
if __name__ == '__main__':
    main()