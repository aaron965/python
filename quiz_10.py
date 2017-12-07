# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by Aaron Albert for COMP9021


from operator import is_not
from functools import partial
import sys
from random import seed, sample
from priority_queue_adt import *


# Possibly define some functions
    
def preferred_sequence():
    L1 = L[:]
    L2,L3,L4,L5 = [], [], [], []

    for e in pq._data:
        L2.append(e)
        if e != None:
            L3.append(e)

    L3.insert(0,None)
    
    i = length 
    
    while i >= 1:
        if i == 1:
            L4.append(L3[i])
            L3.pop(i)
            L5.reverse()
            for items in L5:
                L3.remove(items[1])
                L3.insert(items[0], items[1])
            L5 = []
            i = len(L3) - 1

        if i % 2 == 0 :
            if i + 1 < len(L3) :
                brother = i + 1
            else:
                brother = -1
        else:
            brother = i - 1
        
        parent = i // 2
        if brother == -1:
            L5.append((parent, L3[i]))
            i = parent
            continue

        if L3[i] is not None and L3[brother] is not None and L3[i] > L3[brother] :
            L5.append((parent, L3[i]))
            i = parent
            continue
            
        else:
            L4.append(L3[i])
            L3.pop(i)
            L5.reverse()
            for items in L5:
                L3.remove(items[1])
                L3.insert(items[0], items[1])
            L5 = []
            i = len(L3) - 1
            
    L4.reverse()
    return L4

    # Replace pass above with your code (altogether, aim for around 24 lines of code)


try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())
