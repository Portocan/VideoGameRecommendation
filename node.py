class Node:

    def __init__(self, value, next_node=None): # setting value and default next node
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node): # setting next node
        self.next_node = next_node

    def get_next_node(self): # getting next node
        return self.next_node

    def get_value(self): # getting value
        return self.value