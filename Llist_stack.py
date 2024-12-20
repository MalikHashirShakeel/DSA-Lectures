from Linked_lists import ListNode

class Stack:
    def __init__(self ,max_stk):
        self.stack_head = None
        self.max_stk = max_stk
        self.tos = 0

#----------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        s = f"Current TOS : {None if self.stack_head is None else self.stack_head.data}.\n"
        s += f"Maximum capacity : {self.max_stk}.\n"
        s += f"Occupied capacity : {self.tos}.\n"
        s += f"Remaining capacity : {self.max_stk - self.tos}."
        return s

#----------------------------------------------------------------------------------------------------------------------

    def is_full(self):
        return self.tos == self.max_stk
    
#----------------------------------------------------------------------------------------------------------------------
    
    def is_empty(self):
        return self.tos == 0
    
#----------------------------------------------------------------------------------------------------------------------
    
    def __len__(self):
        return self.tos
    
#----------------------------------------------------------------------------------------------------------------------
    
    def push(self ,value):
        assert not self.is_full() ,"Stack overflow."
        new_node = ListNode(value)
        new_node.next = self.stack_head
        self.stack_head = new_node
        self.tos += 1

#----------------------------------------------------------------------------------------------------------------------

    def pop(self):
        assert not self.is_empty() ,"Stack underflow."
        item = self.stack_head.data
        self.stack_head = self.stack_head.next
        self.tos -= 1
        return item

#----------------------------------------------------------------------------------------------------------------------

#DRIVER CODE
# s1 = Stack(5)
# print(s1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.pop()
# print(s1)