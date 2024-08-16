#Start of the sudoku game
#This is an interactive game, not an automatic sudoku solver, you will have to input numbers yourself
''' After your first game delete the sudoku table array and remove the hashtag from the sudoku_table =np.loadtxt ...  This is to emavle you to load up your saved game  '''

import numpy as np

#example set
sudoku_table = np.array([[0,1,0,0,4,0,0,5,0],[4,0,7,0,0,0,6,0,2],[8,2,0,6,0,0,0,7,4],[0,0,0,0,1,0,5,0,0],[5,0,0,0,0,0,0,0,3],[0,0,4,0,5,0,0,0,0],[9,6,0,0,0,3,0,4,5],[3,0,5,0,0,0,8,0,1],[0,7,0,0,2,0,0,3,0]] )

#sudoku_table = np.loadtxt('sudoku_table.txt')

#check 0 in an np.array
#there are no empty cells in np.array
#cells with no digits have been intialized to 0, so it follows that the completed grid would have no 0 cells 
def check_zero(table):
    return np.any(table == 0)
    
#prints out table/grid
def _print_table(table):
    print(table)

#function to check the row
def check_row(grid):
    #a cell is defined by the sequence [row , column]. we want to check all the cells and compare the individual elements in the cell.
    # sca is our row, so to speak, it increases after every while loop is executed, which means it moves to the next row
    #grid[i,j] where i is the current row and j is the column is a particular cell and is assigned to no
    #we want to check 'no'' against all cells in the grid, which is why k,l represents a similar sequence. ij is the number we need kl is every individual cell in the row
    #if a cell is equal to another and the position of the cell is different the function returns False since it means that there are multiple digits in that cell
    sca =0
    while sca < len(grid):
        for i in range(sca,sca+1):
            for j in range(0,9):
                no = grid[i,j]
                for k in range(sca,sca+1):
                    for l in range(0,9):
                        if no == grid[k,l] and (i,j) != (k,l):
                            return False
        sca+=1                    
    return True

#column checker
#the same logic lies with the row checker, kay is our first column an we need to check every cell in a particular column.
#a grid sequence is in the form [row,column]. here the column is fixed and its the row that changes 
#a list comprehension is written to this effect i is the outer for loop and is fixed, the column. j is the changing row
#initializing the dictionary, the dictionary would contain column index as keys and a list of elements as values
def check_column(grid):
    length  = len(grid)
    kay = 0
    dicc={}
    #grouping the column into a list
    #now we have a list of columns
    while kay < length:
        lst = [grid[j,i] for i in range(kay,kay+1) for j in range(0,9)]
        dicc[kay]=lst
        kay += 1
    
    #this is a little complex, we will be transversing throughout the entire grid
     
    #if a cell [row, column] is in dictionary[column] and the row number is not equals the the cell number undergoimg the search, it means there are double entries in that column
    for i in range(0,9):
            for j in range(0,9):
                if grid[i,j] in dicc[j] and i != dicc[j].index(grid[i,j]):
                    return False
    return True         
               

#in a 9x9 grid the are 9 subgrids each with a dimension of 3x3, each elements must be different from the other
#the list grids are [0-3] [3-6] [6-9], a simple for loop to slice  out the subgrids, place them as values in a dictionary is implemented
#then we want to flattem out this array and convert to a set which would then be compared to a set of 9 digits(1-9), since each set much contain unique elemnts
#if the flattened set equals the set of 9 digits then the function returns true any other thing it returns False
def check_subgrid(table):
    j=0
    duck={}
    for char in[(0,3),(3,6),(6,9)]:
        for brar in [(0,3),(3,6),(6,9)]:
            duck[j]=table[char[0]:char[1],brar[0]:brar[1]]
            j+=1  
       
    lst=[values.flatten().tolist() for keys,values in duck.items()]
    for item in lst:
       if set(item) != set(range(1,10)):
           return False
    return True

def completed_game(table):
    if check_subgrid(table) and check_row(table) and check_column(table):
        return True
    return False
    



print('Welcome, Enjoy your game')    
while check_zero(sudoku_table):
    print('Options: ','1. Pick a Number ','2. Delete a number', '3. End game ',sep='\n')
    
    #note that input function returns a string
    print('')
    choice = input('Enter Choice: ')
    if choice == '1' or choice=='2': 
        _print_table(sudoku_table)
        print('')
        print('Enter the row and column number: ')
        row = input('Row: ')
        column = input('Column: ')
        print('')
        cell_number = input('Input number to be inserted: ')
        row, column, cell_number = int(row),int(column), int(cell_number)
        if cell_number >= 10:
            print('')
            print('Pick Another number')
        else:            
            sudoku_table[row,column] = cell_number
        _print_table(sudoku_table)
        print('')
       
      
    else:
        break
    
if completed_game(sudoku_table):
    print('Game completed')
else:
    print('Game Failed')

np.savetxt('sudoku_table.txt',sudoku_table, fmt = '%d')