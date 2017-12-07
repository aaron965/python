# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M, and
# - when leaves in T are expanded to 2 leaves in T*, those 2 leaves receive the same value.
#
# Written by Aaron Albert for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
   # print(tree.value)
   # print(tree.right_node.value)
   # print(tree.right_node.right_node.value)
   # print(tree.left_node.value)
   # print(tree.height())
    if tree.value is None:
        return
    Max_Sum=Total(tree)
    Expectd_Total = max(Max_Sum)
    print("Max",max(Max_Sum))
    Making_Total(tree,Expectd_Total)
    # Replace pass above with your code


# Possibly define other functions
def Making_Total(tree,Expected):

    if tree.value is None:
        return
    else:
        Expected = Expected - tree.value
        if tree.left_node.value is  None and tree.right_node.value is None:
            if Expected:
                tree.left_node.insert_in_bst(Expected)
                tree.right_node.insert_in_bst(Expected)
        elif tree.left_node.value is  None:
            if Expected:
                tree.left_node.insert_in_bst(Expected)
        elif tree.right_node.value is None:
            if Expected:
                tree.right_node.insert_in_bst(Expected)
        if tree.left_node.value:
            Making_Total(tree.left_node,Expected)
        if tree.right_node.value:
            Making_Total(tree.right_node,Expected)
        return Expected 



        
def Total(Root,total = 0,sum_values=[]):
    if Root.value is None:
        return 
    total+=Root.value
    #print("Roor",Root.value)
    sum_values = set(sum_values)
    sum_values= list(sum_values)
    if Root.left_node.value != None:
        #print("Total",total)
        sum_values+=Total(Root.left_node,total)
       # sum_values.append(total)
    else:
        sum_values.append(total)
        #print("Return Left Total",sum_values)
    
    if Root.right_node.value != None:
     #   print("Total",total)
    #    sum_values = set(sum_values)
     #   sum_values= list(sum_values)
        sum_values+=Total(Root.right_node,total)
      #  sum_values.append(total)
    else:
        sum_values.append(total)
        #print("Return Right Total",sum_values)
    
    #print("Return Total",sum_values)
    return sum_values
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()


