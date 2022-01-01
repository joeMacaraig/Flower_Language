from linked_list import Node, LinkedList

#create hash map class
class HashMap: 
    def __init__(self, size):
        self.array_size = size 
        self.array = LinkedList()
        