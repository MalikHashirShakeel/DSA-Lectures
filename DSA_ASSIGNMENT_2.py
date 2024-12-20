from Linked_lists import ListNode
from Linked_Structures import biuld_list

#-----------------------------------------------------------------------------------------------------------------------------

def del_x(head ,value):
    if head == None:
        return None
    
    if head.data == value:
        while head is not None and head.data == value:
            temp = head
            head = head.next
            temp.next = None

        if head is None:
            return None
        
    node = head
    while node.next is not None:
        if node.next.data == value:
            temp = node.next
            node.next = temp.next
            temp.next = None
        else:
            node = node.next
    return head

#-----------------------------------------------------------------------------------------------------------------------------

#Count the number of nodes having value in its data
def count_x(head ,value):
    node = head
    count = 0

    while node is not None:
        if node.data == value:
            count += 1

    return count

#----------------------------------------------------------------------------------------------------------------------------

#Delete the last node if the list.
def del_tail(head):
    if head is None:
        return None
    elif head.next is None:
        return None
    
    head_node = head
    node = head_node

    while node.next.next is not None:
        node = node.next

    node.next = None
    return head_node

#----------------------------------------------------------------------------------------------------------------------------

def combine(L1 ,L2):
    if L1 is None:
        return L2
    
    head_node = L1
    node = head_node

    while node.next is not None:
        node = node.next

    node.next = L2
    return head_node
    
#-----------------------------------------------------------------------------------------------------------------------------

def split_list(head):
    if head == None:
        return None
    
    head_node = head
    node = head_node

    while node is not None and node.data >= 0:
        node = node.next

    if node is None:
        return head_node ,None

    next_head = node.next
    node.next = None
    return head_node ,next_head

#------------------------------------------------------------------------------------------------------------------------------

def insB4tail(head ,value):
    if head is None:
        return None
    
    elif head.next is None:
        new_node = ListNode(value)
        new_node.next = head
        return new_node

    head_node = head
    node = head_node
    new_node = ListNode(value)

    while node.next.next is not None:
        node = node.next

    temp = node.next
    node.next = new_node
    new_node.next = temp
    return head_node

#------------------------------------------------------------------------------------------------------------------------------

def newHead(head ,value):
    new_head = ListNode(value)
    new_head.next = head
    return new_head

#-----------------------------------------------------------------------------------------------------------------------------


    
