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
        # loop through each of the values
        # compare values
        # return largest