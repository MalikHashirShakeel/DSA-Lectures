import ctypes

class Array:
    def __init__(self,n):#Initializing the array
        assert n > 0,"Size of array must be greater than zero."

        self.size = n
        self.elements = (ctypes.py_object * n)()
        self.clear(None)

    #Checking the length of array.
    def __len__(self):
        return self.size
    
    #Getting the value through indexing.
    def __getitem__(self,index):
        assert index >= 0 and index < self.size,"Please give the value within the range."

        return self.elements[index]
    
    #Setting the value through indexing.
    def __setitem__(self,index,value):
        assert index >= 0 and index < self.size,"Please give the value within the range."

        self.elements[index] = value

    #Inserting a value in the array.
    def insert(self,index,value):
        assert index >= 0 and index < self.size,"Please give the value within the range."

        for item in range(self.size - 1 ,index , -1):
            self.elements[item] = self.elements[item - 1]

        self.elements[index] = value

    #Deleting a value from the array.
    def delete(self,index):
        assert index >= 0 and index < self.size,"Please give the value within the range."

        for item in range(index ,self.size - 1):
            self.elements[item] = self.elements[item + 1]

        self.elements[self.size - 1] = None

    #Traversing the entire array.
    def traverse(self):
        for item in range(self.size):
            print(self.elements[item] ,end= " ")
        
        print()

    #Setting all the values of array to a given value.
    def clear(self,value):
        for item in range(self.size):
            self.elements[item] = value