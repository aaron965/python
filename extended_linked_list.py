

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        first_node=self.head
        current_node=self.head
        #current2_node=self.head
        counter = 0
        while current_node:
            tail_node=current_node
            current_node= current_node.next_node
            counter += 1
      #  print(tail_node.value)
      #  print('counter',counter)
      #  while current2_node:
       #     if current2_node.value % 2 !=0:
       #         self.head=current2_node
      #          break
       #     current2_node= current2_node.next_node
        current1_node=self.head
     #   print("C",current1_node.value)
        
        counter_even = 0
        counter_odd = 0
        for i in range(0,counter):
            if current1_node.next_node==None:
                break
         #   print("D",current1_node.value)
            if current1_node.value % 2 == 0:
              counter_even += 1
              if current1_node==self.head:
              #    print("Hi")
                  self.head=self.head.next_node
             # print('counter for even ',counter_even)
              if first_node.value %2!=0:
                  first_node.next_node=current1_node.next_node
            #  self.head = first
        #      print("I",first_node.value)
            #  print("Hello",first_node.next_node.value)
           #  print("F",first_node.next_node.value)
         #     print("Current",current1_node.value)
          #    print("Current Next Node",current1_node.next_node.value)
              tail_node.next_node = current1_node
              current1_node=current1_node.next_node
              tail_node.next_node.next_node = None
              tail_node = tail_node.next_node
              #tail_node=current1_node
              #tail_node=tail_node.next_node
              #tail_node.next_node.value=None
              
            #  print("Tail",tail_node.value)
           #   print("Newcurent",current1_node.value)
            else:
                counter_odd += 1
             #   print('counter for odd',counter_odd)
                first_node=current1_node
              #  print("First next Node value",first_node.next_node.value)
                first_node.next_node=current1_node.next_node
                current1_node=current1_node.next_node
                
             #   print('huiuh',current1_node.value,'selfhead',self.head.value)

     #   current_node=self.head
     #   while current_node:
      #      tail_node=current_node
        #    current_node= current_node.next_node
       #     print(tail_node.value)
        # Replace pass above with your code
    
    
    
