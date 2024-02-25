from Node import Node

class Stack:
    def __init__(self):
       self.height = None

    def push(self, value):
       node = Node(value)
       node.next_node = self.height
       self.height = node
       
    def extend(self,arr):
        for i in arr:
            self.push(i)
        

    def pop(self):
       if self.height is None:
           return None
       else:
           temp = self.height
           self.height = self.height.next_node
           temp.next_node = None
           return temp.data

    def peek(self):
       if self.height is None:
           return None
       else:
           return self.height.data

    def isEmpty(self):
       if self.height is None:
           return True
       else:
           False

    def size(self):
       count = 0
       
       temp = self.height
       
       while temp is not None:
           count += 1
           temp = temp.next_node
       return count