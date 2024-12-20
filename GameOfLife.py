from pyarray import Array


class LifeGrid:
    #Dead cell will be represented by zero whereas live cell with 1.
    DEAD_CELL = 0
    LIVE_CELL = 1

#-------------------------------------------------------------------------------------------------------------------------

    #Initialize a grid of the given number of rows and columns.
    def __init__(self ,rows ,cols):
        self.rows = rows
        self.columns = cols
        self.grid = Array(self.rows)
        for row in range(len(self.grid)):
            self.grid[row] = Array(self.columns)

#-------------------------------------------------------------------------------------------------------------------------

    #Returns the number of rows.
    def no_of_rows(self):
        return self.rows
    
#-------------------------------------------------------------------------------------------------------------------------
    
    #Returns the number of columns.
    def no_of_columns(self):
        return self.columns
    
#--------------------------------------------------------------------------------------------------------------------------
    
    #Set the grid with the given configuration.
    def configure_grid(self ,arr):
        for row in range(self.rows):
            for col in range(self.columns):
                self.grid[row][col] = self.DEAD_CELL

        for cell in arr:
            self.grid[cell[0]][cell[1]] = self.LIVE_CELL 

#---------------------------------------------------------------------------------------------------------------------------

    #Function to print the grid with the current configuration
    def print_grid(self):
        print("+" + "---+" * self.columns)
        
        for row in range(self.rows):
            for col in range(self.columns):
                value = self.grid[row][col] if self.grid[row][col] is not None else "."  
                print(f"| {value:^2}", end=" ") 
            print("|") 
            
            print("+" + "---+" * self.columns)

#---------------------------------------------------------------------------------------------------------------------------

    #Helper function to adjust the starting subgrid of neighbours for an element.
    def adjusting_starting_index(self ,index):
        index = index
        while index - 1 < 0:
            index += 1
        return index - 1
    
#---------------------------------------------------------------------------------------------------------------------------

    #Helper function to adjust the ending subgrid of neighbours for an element.
    def adjusting_ending_index(self ,index ,configuration):
        index = index
        while index + 2 > configuration:
            index -= 1
        return index + 2
    
#---------------------------------------------------------------------------------------------------------------------------

    #Function to count the number of live neighbours for every element.
    def num_live_neighbours(self ,row ,column):
        r_start ,r_end = self.adjusting_starting_index(row) ,self.adjusting_ending_index(row ,self.rows)
        c_start ,c_end = self.adjusting_starting_index(column) ,self.adjusting_ending_index(column ,self.columns)
        count = 0

        for i in range(r_start ,r_end):
            for j in range(c_start ,c_end):
                if i == row and j == column:
                    count += 0
                elif self.grid[i][j] == 1:
                    count += 1
        return count
    
#---------------------------------------------------------------------------------------------------------------------------

    #Function to give configuration after end for every generation.
    def end_generation(self):
        # Create a manual copy of the grid
        copy_grid = Array(self.rows)
        for row in range(self.rows):
            copy_grid[row] = Array(self.columns)
            for col in range(self.columns):
                copy_grid[row][col] = self.grid[row][col]  # Copy each cell value

        for row in range(self.rows):
            for col in range(self.columns):
                live_neighbours = self.num_live_neighbours(row, col)
                
                # Rule 1: Any dead cell with exactly 3 live neighbours becomes a live cell.
                if self.grid[row][col] == self.DEAD_CELL and live_neighbours == 3:
                    copy_grid[row][col] = self.LIVE_CELL
                    
                # Rule 2: Any live cell with fewer than 2 or more than 3 live neighbours dies.
                elif self.grid[row][col] == self.LIVE_CELL and (live_neighbours < 2 or live_neighbours > 3):
                    copy_grid[row][col] = self.DEAD_CELL

        # Update the grid after the generation
        self.grid = copy_grid

        # Print the updated grid
        self.print_grid()

#-----------------------------------------------------------------------------------------------------------------------------

    #Function to print the result of n generations.
    def end_some_generations(self ,n):
        for _ in range(n):
            print(f"END GENERATION {n}:")
            self.end_generation()
            print()

#==========================================================================================================================


g1 = LifeGrid(5 ,5)
configuration = [(1, 2) ,(2 ,1) ,(2 ,2) ,(2, 3)]
g1.configure_grid(configuration)
g1.print_grid()
g1.end_some_generations(3)




        
                 





