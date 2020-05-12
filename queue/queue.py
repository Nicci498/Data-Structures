"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()


# LL
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        return self.storage.add_to_end(value)

    def dequeue(self):
        return self.storage.remove_from_start()

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

    def add_to_end(self, value):
        new_node = Node(value)
        if self.length > 0:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.length += 1
            return self.tail.value
        else:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return self.head.value

    def remove_from_start(self):
        if self.length > 0:
            prev_head = self.head
            self.head = self.head.get_next()
            self.length -= 1
            return prev_head.value
        else:
            return None
