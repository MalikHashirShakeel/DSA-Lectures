from Linked_lists import ListNode

#Insert the value after the given node
def ins_after(node ,head ,value):
    search = head.search(node)
    if search[0] != False:
        search[2].insert(value)

#Insert the value before the given node
def ins_before(node ,head ,value):
    if node == head:
        new = ListNode(value)
        new.next = head
        return new
    found ,parent ,_ = head.search(node)
    if found:
        parent.insert(value)
        return head
    return head

#Deleting the given node.
def del_node(node ,head):
    if node == head:
        head_ptr = head.next
        head.next = None
        return head_ptr
    found ,parent ,_ = head.search(node)
    if found:
        parent.delete()
        return head
    return head
    

#Building a singly Linked list
def biuld_list(arr):
    assert len(arr) > 0, "List is empty."
    head = ListNode(arr[0])
    node = head
    for ptr in range(1 ,len(arr)):
        node.next = ListNode(arr[ptr])
        node = node.next
    return head


#Build the list dynamically by taking inputs explicitly.
def build_list_updated():
    user_ip = input("Enter the element you want to enter (! to exit): ")
    if user_ip == "!":
        return None
    head = ListNode(user_ip)
    node = head
    while True:
        ip = input("Enter the element you want to enter (! to exit): ")
        if ip == "!":
            print(head.printList())
            return head
        node.next = ListNode(ip)
        node = node.next

# lst = build_list_updated()
        
    




