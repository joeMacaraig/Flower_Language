from linked_list import Node, LinkedList

#create hash map class
class HashMap: 
    def __init__(self, size):
        self.array_size = size 
        self.array = [ LinkedList(None) for i in range(size)]
        
    def hash(self, key):
        return sum(key.encode())
    
    def compress(self, hash_code): 
        return hash_code % self.array_size
    
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        load = Node([key, value])
        array_list = self.array[array_index]

        for item in array_list: 
            if key == item[0]:
                item[1] = value
                return
        array_list.insert(load)

        

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        array_list = self.array[array_index]

        for item in array_list:
            if key == item[0]:
                return item[1]
        return None
