# Creates a class to represent a permutation of 1, 2, ..., n for some n >= 0.
#
# An object is created by passing as argument to the class name:
# - either no argument, in which case the empty permutation is created, or
# - "length = n" for some n >= 0, in which case the identity over 1, ..., n is created, or
# - the numbers 1, 2, ..., n for some n >= 0, in some order, possibly together with "lengh = n".
#
# __len__(), __repr__() and __str__() are implemented, the latter providing the standard form
# decomposition of the permutation into cycles (see wikepedia page on permutations for details).
#
# Objects have:
# - nb_of_cycles as an attribute
# - inverse() as a method
#
# The * operator is implemented for permutation composition, for both infix and in-place uses.
#
# Written by Aaron Albert for COMP9021


class PermutationError(Exception):
    def __init__(self, message):
        self.message = message

class Permutation:
    def __init__(self, *args, length = None):
        self.args=args
        self.length=length
        
        count=0
        Values=[]
        for j in self.args:
            if isinstance(j,int)==False:
                raise PermutationError('Cannot generate permutation from these arguments')
            count+=1
            if j < 1:
                raise PermutationError('Cannot generate permutation from these arguments')
            if j < 1 or j > len(self.args):
                raise PermutationError('Cannot generate permutation from these arguments')   
        if self.length:
            if self.args==():
                for m in range(1,length+1):
                    Values.append(m)
                    count+=1
                self.args=tuple(Values)
            if count!=self.length and self.args!=():
                raise PermutationError('Cannot generate permutation from these arguments')
            if len(set(self.args))!=count:
                raise PermutationError('Cannot generate permutation from these arguments')
            if self.length<0:
                raise PermutationError('Cannot generate permutation from these arguments')
        self.nb_of_cycles = len(self.cycles1())  
        # Replace pass above with your code

    def __len__(self):
        count1=0
        for i in self.args:
            count1+=1
        return count1
        pass
        # Replace pass above with your code

    def __repr__(self):
        return f'Permutation{self.args}'
        # Replace pass above with your code

    def __str__(self):
        M=[]
        L2 = []
        if len(self.cycles1())==0:
           return '()'
        M=self.cycles1()
        for items in M:
            myList = ' '.join(map(str, items))
            b = '(' + myList + ')'
            L2.append(b)
        c = ''.join(i for i in L2)
        return c
    
    def cycles1(self):
         L=[]
         cycles=[]
         for i in self.args:
            temp=i
            temp1=0
            for j in range(1,len(self.args)+1):
                if temp1!=i:
                    L.append(temp)
                    temp=self.args[temp-1]
                    temp1=self.args[temp-1]
            if temp not in L:
                L.append(temp)
            cycles.append(tuple(L))
            L=[]
         N=list(cycles)
         for i in range(0,len(cycles)):
                if len(cycles[i]) > 1:
                    if cycles[i][0]<cycles[i][1]:
                        N.remove(cycles[i])
                    else:
                        temp=cycles[i][0]
                        for j in range(0,len(cycles[i])):
                            if temp<cycles[i][j]:
                                N.remove(cycles[i])
                                break
         N=sorted(N,key=lambda x:x[0])
         return (N)
        # Replace pass above with your code

    def __mul__(self, permutation):
        L=[]
        p=self.args
        q=permutation.args
        if len(self.args) != len(permutation.args):
            raise PermutationError('Cannot compose permutations of different lengths')
        for i in p:
            L.append(q[i-1])
        o =tuple(L)
        return Permutation(*o)
    
        # Replace pass above with your code

    def __imul__(self, permutation):
        o=[]
        p=self.args
        q=permutation.args
        if len(self.args) != len(permutation.args):
            raise PermutationError('Cannot compose permutations of different lengths')
        for i in p:
            o.append(q[i-1])
        p=tuple(o)
        return Permutation(*p)
        # Replace pass above with your code

    def inverse(self):
        o=[]
        for i in range(1,len(self.args)+2):
            for j in range(0,len(self.args)):
                if self.args[j]==i-1:
                    o.append(j+1)
        o=tuple(o)
        return Permutation(*o)
        # Replace pass above with your code
        
    # Insert your code for helper functions, if needed



                
        
