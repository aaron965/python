# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Aaron Albert for COMP9021


import sys
from random import seed, randrange

from stack_adt import *


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))
Total=0
Paths=Stack()
# Garbage value to Pop First Tie You Enter The Loop

def explore_depth_first(x, y, target):
    global Total,Paths
    temp=[]
    temp_values = []
    count=0
    North_prev=None
    East_prev=None
    South_prev=None
    West_prev=None
    
    if target > 0:
        Paths.push((x,y))
        temp.append((x,y))
        #temp_values.append((x,y))
        
    while Total < target and not Paths.is_empty():

    #To Pop The Values Until List Is Empty
        count+=1
        Popped_Element=Paths.pop()
        temp.remove(Popped_Element)
        #print("Paths",Paths._data)
        x=Popped_Element[0]
        y=Popped_Element[1]
        #print("Popped Element",Popped_Element)
        if count==1000:
            return None
            #print("Hi",x,y)
        if Total:
            Total=Total-grid[x][y]
        
    #North
        count=0
        if Total+grid[x][y] > target and y+1 <= 9:
            y=y+1
            #print("Exiting North......")
            
        while Total < target and x > 0:
              #print("North")
              #print("X",x)
              if x and Total<=target:
                if not (x,y) in temp:
                    if Total+grid[x][y] > target:
                       # x=x+1
                        break
                    if North_prev == (x,y) or (x-1,y) == North_prev:
                        break
                    for i in range(0,len(temp_values)):
                        if temp_values[i] == (x,y):
                            #print("True1")
                            try:
                                if temp_values[i+1] == (x-1,y):
                                    #print("True2")
                                    count+=1
                            except IndexError:
                                pass
                    if count > 0:
                        #print('North Break')
                        break
              #      print("North Appending")
               #     print("Grid-----",x,y)
                    Total+=grid[x][y]
                    Paths.push((x,y))
                    temp.append((x,y))
                    temp_values.append((x,y))
                    North_prev=(x,y)
                    #print("North Values",temp_values)
                if (x-1,y) in temp:
                      #print("fhgfhdgf")
                      break
                x-=1
                #if not Total+grid[x][y] <=target or not Total+grid[x][y+1] <=target or not Total+grid[x+1][y] <=target or not Total+grid[x][y-1] <=target:
             #   print("value",x,y)
                   # Total=Total-grid[x][y]
                    #Paths.pop()
                    #break
                #print("Grid",grid[x][y])
                #print("Peek Value",Paths.peek())
                if Total==target:
                    break

    #East
        count = 0
        if Total+grid[x][y] > target and x+1 <= 9:
            #print("grid value",x,y)
            x=x+1
            #print("Exiting East......")
            #print("East Values",x,y)

        
        while Total < target and y < 9:
             #print("East")
             #print("east x y",x,y)
             if y < 10 and Total<=target:
                if not (x,y) in temp:
                    #To Check if Total Value is Greater than Target
                    if Total+grid[x][y] > target:
                        #y=y-1
                        break
                    if East_prev == (x,y) or (x,y+1) == East_prev:
                        #print('true')
                        break
                    #else:
                        #print('false')
                                   
                    for i in range(0,len(temp_values)):
                        if temp_values[i] == (x,y):
                            #print("True1")
                            try:
                                if temp_values[i+1] == (x,y+1):
                                    #print("True2")
                                    count+=1
                            except IndexError:
                                pass
                    if count > 0:
                        #print('East Break')
                        break
             #       print("East Appending")
              #      print("Grid-----",x,y)
                    Total+=grid[x][y]
                    Paths.push((x,y))
                    temp.append((x,y))
                    temp_values.append((x,y))
                    #print("East Values",temp_values)
                    East_prev=(x,y)
                if (x,y+1) in temp:
                    break
                y+=1
                #print("Peek Value 3",Paths.peek())
                if Total==target:
                    break
   #South
        count = 0
        #Checking Last Value From East
                
        if Total+grid[x][y] > target and y-1 >= 0:
            y=y-1
            #print("Exiting South......")
            
        while Total < target and x < 9:
              #print("South")
              if x < 10 and Total<=target:
                #print("X1",x,"Y1",y)
                if not (x,y) in temp:
                    if Total+grid[x][y] > target:
                        #x=x-1
                        break
                    if South_prev == (x,y) or (x+1,y) == South_prev:
                        break

                    for i in range(0,len(temp_values)):
                        if temp_values[i] == (x,y):
                            #print("True1")
                            try:
                                if temp_values[i+1] == (x+1,y):
                                    #print("True2")
                                    count+=1
                            except IndexError:
                                pass
                    if count > 0:
                       # print('South Break')
                        break
                   # print("South Appending")
                    #print("Grid-----",x,y)
                    Total+=grid[x][y]
                    Paths.push((x,y))
                    temp.append((x,y))
                    temp_values.append((x,y))
                    #print("South Values",temp_values)
                    South_prev=(x,y)
                if (x+1,y) in temp:
                    break
                x+=1
               # print("Peek Value 3",Paths.peek())
                if Total==target:
                    break

   #West
        count = 0
        if Total+grid[x][y] > target and x-1 >= 0:
            x=x-1
            #print("Exiting West......")
        count_west=0
        while Total < target and y >= 0:
             count_west+=1
             #print("West")
             #print("Y",y)
             #print("Total",Total)
             if count_west > 11:
              #   print("West Counter")
                 break
             if not y<0 and Total<=target:
                if not ((x,y)) in temp:
                    if Total+grid[x][y] > target:
                        #y=y+1
                        break
                    if West_prev == (x,y) or (x,y-1) == West_prev:
                        break
                                   
                    for i in range(0,len(temp_values)):
                        if temp_values[i] == (x,y):
                            #print("True1")
                            try:
                                if temp_values[i+1] == (x,y-1):
                             #       print("True2")
                                    count+=1
                            except IndexError:
                                pass
                    if count > 0:
                        #print('West Break')
                        break
                    #print("West appending")
                    #print("Grid-----",x,y)
                    Total+=grid[x][y]
               #     print("Total--",Total)
                    Paths.push((x,y))
                    temp.append((x,y))
                    temp_values.append((x,y))
                   # print("West Values",temp_values)
                    West_prev=(x,y)
                else:
                #    print("West too")
                    break
                if (x,y-1) in temp:
                    break
                y-=1
            #    print("Peek Value",Paths.peek())
                if Total==target:
                    break
        
    return Paths._data

    # Replace pass above with your code


try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)
