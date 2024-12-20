class Stack:
    def __init__(self, max_stk):
        self.stack = []
        self.max_stack = max_stk
        self.tos = -1

    #------------------------------------------------------------------------------------------------------------------

    def __repr__(self):
        s = "Stack Representation:\n"
        if not self.stack:
            s += "| Empty Stack |\n"
        else:
            s += "Top ->\n"
            for item in reversed(self.stack):
                s += f"| {item} |\n"
            s += "__\n"
        
        s += f"Max Capacity: {self.max_stack}, Current Size: {len(self.stack)}"
        return s

    #------------------------------------------------------------------------------------------------------------------

    def __len__(self):
        return self.tos + 1

    #------------------------------------------------------------------------------------------------------------------

    def get_info(self):
        print(f"Max Capacity : {self.max_stack}")
        print(f"Top of Stack : {self.stack[self.tos] if self.stack != [] else None}")
        print(f"Occupied capacity : {self.tos + 1}")
        print(f"Remaining capacity : {self.max_stack - (self.tos + 1)}")

    #------------------------------------------------------------------------------------------------------------------

    def push(self, item):
        assert self.tos < self.max_stack - 1, "Stack Overflow."
        self.stack.append(item)
        self.tos += 1
        print(f"Pushed item : {item}")
        print(f"Remaining capacity : {self.max_stack - (self.tos + 1)}")

    #------------------------------------------------------------------------------------------------------------------

    def pop(self):
        assert self.tos > -1, "Stack Underflow."
        item = self.stack.pop()
        self.tos -= 1
        print(f"Popped item : {item}")
        print(f"Remaining capacity : {self.max_stack - (self.tos + 1)}")
        return item

    #------------------------------------------------------------------------------------------------------------------

    def peek(self):
        return self.stack[-1] if self.tos != -1 else "Empty Stack."

    #------------------------------------------------------------------------------------------------------------------

    def is_empty(self):
        return self.tos == -1

    #------------------------------------------------------------------------------------------------------------------

    def is_full(self):
        return self.tos == self.max_stack - 1

    #------------------------------------------------------------------------------------------------------------------

    def clear_stack(self):
        self.stack.clear()
        self.tos = -1

#======================================================================================================================

# Driver Code
# s1 = Stack(6)
# s1.get_info()
# s1.push(10)
# s1.push(20)
# print(s1)
# s1.pop()
# s1.peek()
# s1.pop()
# # s1.pop()
# print(s1.is_empty())
# s1.push(1)
# s1.push(2)
# s1.push(3)
# s1.push(4)
# s1.push(5)
# s1.push(6)
# # s1.push(7)
# print(s1.is_full())
# s1.clear_stack()
# s1.get_info()

# s2 = Stack(4)
# s2.clear_stack()
# x = 4
# z = 0
# y = x + 1
# s2.push(y)
# s2.push(y + 1)
# s2.push(x)
# y = s2.pop()
# x = y + 1
# s2.push(x)
# s2.push(z)
# while not s2.is_empty():
#     z = s2.pop()
#     print(z)
# print("X : ",x)
# print("Y : ",y)
# print("Z : ",z)
