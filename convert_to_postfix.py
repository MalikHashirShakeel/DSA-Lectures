from stack import Stack

def has_heigher_precedence(e1 ,e2):
    preced = {"+" : 1 ,"-" : 1 ,"*" : 2 ,"/" : 2 ,"^" : 3}
    return preced[e1] > preced[e2]

#----------------------------------------------------------------------------------------------------------------------

def empty_parenthesis(stk, arr):
    while not stk.is_empty() and stk.peek() != "(":
        arr.append(stk.pop())
    if not stk.is_empty():
        stk.pop() 

#----------------------------------------------------------------------------------------------------------------------

def clear_remaining_stack(stk, arr):
    while not stk.is_empty():
        arr.append(stk.pop())

#----------------------------------------------------------------------------------------------------------------------

def fill_into_stack(stk, item, arr):
    while not stk.is_empty() and stk.peek() != "(" and not has_heigher_precedence(item, stk.peek()):
        arr.append(stk.pop())
    stk.push(item)

#----------------------------------------------------------------------------------------------------------------------

def convert_to_postfix(lst):
    assert len(lst) > 0, "Empty input list."
    arr = []
    stk = Stack(len(lst)) 

    for item in lst:
        if isinstance(item, int): 
            arr.append(item)

        elif item == "(":  
            stk.push(item)

        elif item == ")":
            empty_parenthesis(stk, arr)

        else: 
            fill_into_stack(stk, item, arr)

    clear_remaining_stack(stk, arr)  
    return arr

#----------------------------------------------------------------------------------------------------------------------

l1 = [3 ,"+" ,4 ,"*" ,5]
l2 = ["(" ,3 ,"+" ,4 ,")" ,"*" ,5]
l3 = [8 ,"+" ,9 ,"-" ,"(" ,5 ,"-" ,2 ,")" ,"*" ,"(" ,"(" ,1 ,"-" ,7 ,")" ,"+" ,4 ,")" ,"/" ,2]
print(convert_to_postfix(l3))



