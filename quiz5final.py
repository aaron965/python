# Randomly fills a grid of size height and width whose values are input by the user,
# with nonnegative integers randomly generated up to an upper bound N also input the user,
# and computes, for each n <= N, the number of paths consisting of all integers from 1 up to n
# that cannot be extended to n+1.
# Outputs the number of such paths, when at least one exists.
#
# Written by Aaron Albert for COMP9021

l=[]
from random import seed, randint
import sys
from collections import defaultdict,Counter

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def get_paths():
    c={k:v for k,v in Counter(b).items() if v>0}
    return c

    # Replace pass above with your code
    # Insert your code for other functions
    
def get_areas(i,j):
    global l
    temp=grid[i][j]
 
    if j and grid[i][j-1] > 0 and grid[i][j-1]==temp+1:
        get_areas(i,j-1)
    if j < width-1 and grid[i][j+1] > 0 and grid[i][j+1]==temp+1:
        get_areas(i,j+1)
    if i and grid[i-1][j] > 0 and grid[i-1][j]==temp+1:
        get_areas(i-1,j)
    if i < height-1 and grid[i+1][j] > 0 and grid[i+1][j]==temp+1:
        get_areas(i+1,j) 
        
    l.append(grid[i][j])
    return (grid[i][j])
        
try:
    for_seed, max_length, height, width = [int(i) for i in
                                                  input('Enter four nonnegative integers: ').split()
                                       ]
    if for_seed < 0 or max_length < 0 or height < 0 or width < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randint(0, max_length) for _ in range(width)] for _ in range(height)]
print('Here is the grid that has been generated:')
display_grid()


for i in range(height):
    for j in range(width):
        if grid[i][j] == 1:
           a= get_areas(i,j)
        
#print(l)
b=l[:]           
for i in range(0,len(l)-1):
    if l[i+1]<l[i]:
        b.remove(l[i+1])    
    
paths = get_paths()
if paths:
    for length in sorted(paths):
        print(f'The number of paths from 1 to {length} is: {paths[length]}')

