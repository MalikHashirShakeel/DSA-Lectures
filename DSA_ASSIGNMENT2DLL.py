from doublyLinkedList import DoublyListNode
from Linked_lists import ListNode
from Linked_Structures import biuld_list

def insertInDList(head ,x ,value):
    current = head
    new = DoublyListNode(value)
    while current is not None:
        if current.data == x:
            next_ptr = current.right
            current.right = new
            new.left = current
            new.right = next_ptr
            if next_ptr:
                next_ptr.left = new
            current = new.right
        else:
            current = current.right

    return head



def maxDList(head):
    if not head:
        return None
    current = head
    current_max = current.data
    while current is not None:
        if current.data > current_max:
            current_max = current.data
            current = current.right
        else:
            current = current.right
    return current_max


def ins_in_c_list(head ,x ,value):
    if not head:
        return None
    current = head
    while current.next != head:
        if current.data == x:
            new = ListNode(value)
            next_ptr = current.next
            current.next = new
            new.next = next_ptr
            current = new.next
        else:
            current = current.next
    return head





