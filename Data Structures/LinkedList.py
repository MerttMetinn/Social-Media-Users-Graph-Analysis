from Node import Node


class LinkedList:
    def __init__(self):
        self.root = None

    def isEmptyList(self):
        if self.root is None:
            return True
        else:
            return self.root is None

    def add(self, data):
        
        new_node = Node(data)
        
        if self.root is None:
            
            self.root = new_node
            
        else:
            
            last_node = self.root
            
            while last_node.next_node != None:
                last_node = last_node.next_node
                
            
            last_node.next_node = new_node

    def delete(self, data):
        current = self.root

        if current and current.data == data:
            self.root = current.next_node
            current = None
            return 1

        prev_node = None
        while current and current.data != data:
            prev_node = current
            current = current.next_node

        if current is None:
            return

        prev_node.next_node = current.next_node
        current = None

    def display(self):
        current_node = self.root
        while current_node is not None:
            print(current_node.data, end="->")
            current_node = current_node.next_node
        print("None\n",end="")
        
    def __str__(self):
        laststr = "["
        current_node = self.root
        while current_node:
            laststr+=current_node.data+","
            current_node = current_node.next_node
            
        laststr = laststr[:-1]
        laststr+="]"
        
        return laststr
        
    def __iter__(self):
        self.current_node = self.root
        return self

    def __next__(self):
        if self.current_node:
            data = self.current_node.data
            self.current_node = self.current_node.next_node
            return data
        else:
            raise StopIteration
        
        
