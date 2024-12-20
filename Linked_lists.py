class ListNode:
    #Instentiate a new node.
    def __init__(self ,value):
        self.data = value
        self.next = None

    #Representation of the object.
    def __repr__(self):
        return f"|{self.data}| |"
    
    #Function to insert a node next to the current node.
    def insert(self ,value):
        #Instentiate the object with the given value
        node = ListNode(value)
        #The node next to it will become the the node next to the object because the inserting node will come in between.
        node.next = self.next
        #The inserting node will be next to this current node.
        self.next = node

    #Function to delete the node next to the current node.
    def delete(self):
        #Checking if the node is not the last node.
        if self.next is not None:
            #creating a variable for new node.
            temp = self.next
            #The node we want to retrive.
            item = temp.data
            #set the next of this node to the node after the deleting node.
            self.next = temp.next
        #return the node we want to delete
        return item
    
    #Function to count the length of the linked list.
    def __len__(self):
        #Made a variable for head node.
        node = self
        #initialize count to 0.
        count = 0
        #increment count until the node is not the last.
        while node is not None:
            count += 1
            #shift the node to next
            node = node.next
        
        #return the length of list
        return count
    
    #Function to search a node in the list.
    def search(self ,target):
        #make a variable for the head node.
        a = self
        #check if the element is found a first occurence
        if a.data == target:
            return True ,None ,a
        #make a variable for the current occurence ,a eill now become the parent.
        b = self.next
        #iterate until the last node reaches.
        while b is not None:
            #increment both a and b
            a = a.next
            b = b.next
        #return the if the element is present(true/false) ,its parent ,and node itself.
        return b is not None ,a ,b
    
    #Function to print the linked list.
    def printList(self):
        #Make a variable for head node
        node = self
        #make an empty list
        nodes = []
        #iterate until the last node
        while node is not None:
            #append each node's data to the list.
            nodes.append(f"|{node.data}|  |")
            #Increment the node
            node = node.next
        #At last , append none.
        nodes.append("None")
        #Return the result to print.
        return "->".join(nodes)

    #Function to make the linked list circular
    def make_circular(self):
        current = self
        while current.next is not None:
            current = current.next
        current.next = self

    #Function to traverse the circular linked list
    def traverse_circular(self):
        current = self
        while current.next != self:
            print(current.data)
            current = current.next
        print(current.data)

    #Function to make the circular linked list linear
    def make_linear(self):
        current = self
        while current.next != self:
            current = current.next
        current.next = None
        return self
        


#TEST RUN
    
# head_node = ListNode("0")
# node_1 = ListNode("1")
# node_2 = ListNode("2")
# node_3 = ListNode("3")
# node_4 = ListNode("4")
# node_5 = ListNode("6")
# node_6 = ListNode("8")
# node_7 = ListNode("7")
# head_node.next = node_1
# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4
# node_4.next = node_5
# node_5.next = node_6
# node_6.next = node_7

# node_4.insert("5")
# print(node_4.next)
# node_5.delete()
# print(node_5.next)

# print(len(head_node))

# print(head_node.search(node_5))
# print(head_node.printList())



