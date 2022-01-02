#create class Node and LinkedList
class Node: 
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value 
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

class LinkedList: 
    def __init__(self, head_node = None):
        self.head_node = head_node
    
    def get_head_node(self):
        return self.head_node
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def remove_node(self, remove_value):
        current_node = self.get_head_node()
        if current_node.get_value() == remove_value: 
            self.head_node = current_node.get_next_node()
        else: 
            while current_node: 
                next_node = current_node.get_next_node()
                if next_node.get_value() == remove_value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None 
                else: 
                    current_node = next_node
    
    def __iter__(self): 
        current_node = self.head_node
        while current_node: 
            yield current_node.get_value()
            current_node = current_node.get_next_node()