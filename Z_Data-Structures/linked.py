from msilib.schema import SelfReg


class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class linked_list: 
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head