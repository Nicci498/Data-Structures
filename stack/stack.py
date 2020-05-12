"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Arr

# class Stack:
#     def __init__(self):
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             print(self.storage)
#             return self.storage.pop()

#LL
class Stack:
    def __init__(self):
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.add_to_top(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_from_top()  

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_top(self, value):
        new_node = Node(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def remove_from_top(self):
        if self.length > 0:
            current = self.head
            previous = None
            while current.next_node != None:
                previous = current
                current = current.get_next()
            if previous != None:
                previous.set_next(None)
                self.tail = previous
                self.length -= 1
                return current.value
            else:
                self.head = None
                self.tail = None
                self.length = 0
                return current.value
        else:
            return None
