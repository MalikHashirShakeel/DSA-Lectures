#Doubly Linked List =>

class DoublyListNode:
    #Constructor to initailize a node in the doubly linked list
    def __init__(self ,value = None):
        self.data = value
        self.left = None
        self.right = None

#-------------------------------------------------------------------------------------------------------------------------

    #A function to insert the node on the right side of the itself.
    def insert_right(self ,value):
        new = DoublyListNode(value)
        if self.right is None:
            self.right = new
            new.left = self
            return 
        next_node = self.right
        self.right = new
        new.left = self
        new.right = next_node
        next_node.left = new

#------------------------------------------------------------------------------------------------------------------------

    #A function to insert the node on the right side of the itself.
    def insert_left(self ,value):
        new = DoublyListNode(value)
        if self.left == None:
            self.left = new
            new.right = self
            return
        prev = self.left
        self.left = new
        new.right = self
        new.left = prev
        prev.right = new

#------------------------------------------------------------------------------------------------------------------------

    def delete(self):
        if not self.left and not self.right:
            return None
        elif self.left is None:
            current = self.right
            current.left = None
            self.right = None
            return current
        current = self.left
        next =self.right
        current.right = next
        if next:
            next.left = current
        self.left = None
        self.right = None
        return current

#------------------------------------------------------------------------------------------------------------------------

            
