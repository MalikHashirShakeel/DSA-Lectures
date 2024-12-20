from pyarray import Array

class Array2D:
    def __init__(self ,rows ,columns):
        self.rows = rows
        self.columns = columns
        self.matrix = Array(rows)
        for row in range(len(self.matrix)):
            self.matrix[row] = Array(columns)

#------------------------------------------------------------------------------------------------------------------------
        
    def printMatrix(self):
        for row in range(len(self.matrix)):
            self.matrix[row].traverse()

#------------------------------------------------------------------------------------------------------------------------

    def numRows(self):
        return self.rows
    
#------------------------------------------------------------------------------------------------------------------------

    def numCols(self):
        return self.columns
    
#------------------------------------------------------------------------------------------------------------------------

    def clear(self ,value):
        for row in range(len(self.matrix)):
            self.matrix[row].clear(value)

#------------------------------------------------------------------------------------------------------------------------

    def __setitem__(self ,index ,value):
        assert len(index) == 2 ,"Please enter a valid index value here."
        self.matrix[index[0]][index[1]] = value

#-------------------------------------------------------------------------------------------------------------------------

    def __getitem__(self ,index):
        assert len(index) == 2 ,"Please enter a valid index value here."
        return self.matrix[index[0]][index[1]]

#------------------------------------------------------------------------------------------------------------------------

    def matmul(self ,other1 ,other2):
        assert other1.columns ==  other2.rows ,"Multiplication not possible!"
        x = other1.numRows()
        y = other2.numCols()
        z = other1.numCols()
        self.clear()
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    self.matrix[i ,j] = self.matrix[i ,j] + other1[i ,k] * other2[k ,j]

#-------------------------------------------------------------------------------------------------------------------------

# mat = Array2D(5 ,5)
# mat[2 ,3] = 1
# mat.printMatrix()
