from stack import Stack

def evaluate_postfix(arr):#O(n)
    #Initialize an empty stack.
    lenght = len(arr)#O(1)
    assert lenght > 0 ,"Empty list."#O(1)
    stk = Stack(lenght)#O(1)

    #Iterate over the entire list.
    for item in range(lenght):#O(n) * O(1) = O(n)
        #If the element is an operand ,simply push it in the stack.
        if isinstance(arr[item] ,int):#O(1)
            stk.push(arr[item])#O(1)
            
        #If the element is an operator.
        else:#O(1)
            #Pop it from the stack and give it a name b.
            b = stk.pop()#O(1)
            #Again pop and give it a name of a.
            a = stk.pop()#O(1)

            #Apply the operation on both a and b and push the result in the stack.
            if arr[item] == "^":#O(1)
                stk.push(a ** b)#O(1)
            elif arr[item] == "*" or arr[item] == "/":#O(1)
                stk.push(a * b) if arr[item] == "*" else stk.push(a / b)#O(1)
            else:#O(1)
                stk.push(a + b) if arr[item] == "+" else stk.push(a - b)#O(1)

    #Pop the result from the stack and return it.
    return stk.pop()#O(1)

# l = [1 ,2 ,"-" ,4 ,5 ,"^" ,3 ,"*" ,6 ,"*" ,2 ,2 ,2 ,"^" ,"^" ,"/" ,"-"]
# l2 = [4 ,12 ,11 ,9 ,"*" ,9 ,"-" ,6 ,"+" ,12 ,"/" ,"+" ,"-"]
# print(evaluate_postfix(l2))