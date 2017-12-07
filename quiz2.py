
# Written by Aaron Albert for COMP9021

'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd
from fractions import Fraction

try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
M=[]
N=[]
spot_on, closest_1, closest_2 = [None] * 3

# Replace this comment with your code
for i in range(0,length):
    for j in range(0,length):
        if L[i]==0 or L[j]==0:
            if 0 not in M:
                fractions.append(0)
                M.append(0)
        elif L[i] <= L[j]:
            num1= Fraction(L[i],L[j])
        else:
            num1= Fraction(L[j],L[i])
        if num1 not in M:
            if int(num1) <= 1:    
                fractions.append(num1)
                M.append(num1)
              
fractions.sort()
M.sort()

for i in range(0,len(fractions)):
    fractions[i]=str(fractions[i])
    
#To find the numbers equal to 1/2
            
if 1/2 in M:
    spot_on=True
elif len(M)==1:
    closest_1=M[0]
else:
     for i in range(0,len(M)):
         N.append(abs(Fraction(1,2)-M[i]))
     num=min(N) 
               
     for i in range(0,len(N)):            
         if N[i]==num and N[i+1]==num:
             closest_1=M[i]
             closest_2=M[i+1]
             break
         elif N[i]==num:
             closest_1=M[i]
             
print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

