"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # What are we doing either way?
        # wrap val in a node and add to length
        new = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # set new node to head and tail
            self.head = new
            self.tail = new
        else:
            # set the new nodes next pointer to the old head
            new.next = self.head
            # set the old head's prev pointer to new node
            self.head.prev = new
            # update the head to the new node
            self.head = new
        

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # wants the value returned so we set that to a variable
        value = self.head.value
        # we utilize our list delete on the head
        self.delete(self.head)
        #and return the value we saved
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new
            self.tail = new            
        else:
            # set the old tails pointer to new node
            # new is already set to none
            self.tail.next = new
            # set new's prev to old tail
            new.prev = self.tail
            # update the tail to equal new
            self.tail = new

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # save the value to return
        value = self.tail.value
        # del tail
        self.delete(self.tail)
        # give em what they want
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #if not already head
        if node is self.head:
            return
        #save the val of node
        value = node.value
        #delete from where it is        
        self.delete(node)
        #add to head
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        self.length -=1
        #if both set head/ tail to none
        if self.head is self.tail:
            self.head = None
            self.tail = None
        #if head set head pointer to 2nd ele, and delete old head
        elif node is self.head:
            self.head = self.head.next
            node.delete()
        #if tail set prev node to tail and delete old tail
        elif node is self.tail:
            self.tail = self.tail.prev
            node.delete()              
        #if reg node
        else:
            node.delete()
        
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head and not self.tail:
            return None
        max = self.head.value
        current = self.head
        while current:
            if current.value > max:
                max = current.value
            current = current.next
        return max
        # loop through each of the values
        # compare values
        # return largest

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        #self.size = 0
        self.order = DoublyLinkedList()
        self.storage = dict()


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        #key is not in cache -return none
        if key not in self.storage:
            return None
        else:
        #key is in cache            
            #move it to most recently used
            node = self.storage[key]
            self.order.move_to_end(node)
            # #return value
            return node.value[1]


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if item/key already exist
        if key in self.storage:
            # overwrite the val
            # where is value stored
            node = self.storage[key]
            node.value = (key, value)
            # move to tail as most recently used
            self.order.move_to_end(node)
            return
        #size is at limit
        if len(self.order) == self.limit:
            # remove oldest
            oldest_index = self.order.head.value[0]
            del self.storage[oldest_index]
            self.order.remove_from_head()

        #add to order
        self.order.add_to_tail((key, value))
        #add to storage
        self.storage[key] = self.order.tail
        
        

            
        
        
        
