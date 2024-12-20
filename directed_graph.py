from Vertex import Vertex
from Edge import Edge

class Graph:
    def __init__(self, vertices):
        # Initialize the vertices list and adjacency/weight matrices
        self._vertices = vertices
        self._head_vertex = Graph.vertices_list(vertices)
        self._adjacency_matrix = None  # Matrix to indicate direct edges between vertices (1 or 0)
        self._weight_matrix = None     # Matrix to store edge weights between vertices
        self._nodes_matrix = None
        self._path_matrix = None
        self._shortest_paths = None
        self._shortest_path_nodes = None
        self._adjacency_table = None
        # Dictionary to map vertex names to their indices in the matrices
        self._vertex_indices = {key: idx for idx, key in enumerate(vertices)}

#-------------------------------------------------------------------------------------------------------------------------

    def num_vertices(self):
        # Returns the number of vertices in the graph
        return len(self._vertices)

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def vertices_list(vertices_arr):
        # Builds a linked list from an array of vertices and returns the head vertex
        head_vertex = Vertex(vertices_arr[0])  # Initialize with the first vertex
        vertex = head_vertex

        # Link each vertex to the next to form a linked list
        for idx in range(1, len(vertices_arr)):
            vertex.next = Vertex(vertices_arr[idx])
            vertex = vertex.next  # Move to the new vertex

        return head_vertex  # Return the head of the list

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def find_node(head, target):
        # Searches for a vertex by key within the linked list, starting from head
        node = head
        while node is not None and node.key != target:
            node = node.next

        return node  # Returns the node if found; otherwise, None
    
#-------------------------------------------------------------------------------------------------------------------------

    def add_edge(self, tuple_data):
        # Adds a directed edge between two vertices with a specified weight
        edge_value, parent_key, destination_key = tuple_data
        edge = Edge(edge_value)

        # Find the source (parent) and destination vertices
        parent_vertex = Graph.find_node(self._head_vertex, parent_key)
        destination_vertex = Graph.find_node(self._head_vertex, destination_key)

        if parent_vertex is not None and destination_vertex is not None:
            edge.vertex = destination_vertex  # Link edge to destination vertex
            current_edge = parent_vertex.edge

            # If no edges exist from the source, add this edge as the first one
            if current_edge is None:
                parent_vertex.edge = edge
            else:
                # Otherwise, traverse to the end and add the new edge
                while current_edge.next is not None:
                    current_edge = current_edge.next
                current_edge.next = edge

#-------------------------------------------------------------------------------------------------------------------------

    def print_graph(self):
        # Prints each vertex and its edges
        vertex = self._head_vertex
        while vertex is not None:
            edges = []
            current_edge = vertex.edge
            while current_edge is not None:
                edges.append(str(current_edge))  # Format: destination vertex and weight
                current_edge = current_edge.next
            edges_str = ' '.join(edges) if edges else "| None |"  # If no edges, show None
            print(f"{vertex} {edges_str} | None |")
            vertex = vertex.next

#-------------------------------------------------------------------------------------------------------------------------

    def adj_mat(self):
        # Generates the adjacency matrix (1 if edge exists, 0 otherwise)
        length = self.num_vertices()
        mat = [[0 for _ in range(length)] for _ in range(length)]
        vertex = self._head_vertex

        # Populate the adjacency matrix
        while vertex is not None:
            parent_index = self._vertex_indices[vertex.key]
            current_edge = vertex.edge

            # Mark connections in the matrix based on edges
            while current_edge is not None:
                destination_index = self._vertex_indices[current_edge.vertex.key]
                mat[parent_index][destination_index] = 1  # Indicate direct edge
                current_edge = current_edge.next

            vertex = vertex.next

        self._adjacency_matrix = mat  # Store the matrix in the instance

#-------------------------------------------------------------------------------------------------------------------------

    def print_adj(self):
        # Prints the adjacency matrix
        print("ADJACENCY MATRIX:")
        for row in range(len(self._adjacency_matrix)):
            for col in range(len(self._adjacency_matrix)):
                print(f"{self._adjacency_matrix[row][col]}", end=" ")
            print()

#------------------------------------------------------------------------------------------------------------------------

    def print_nodes_mat(self):
        print("PATHS BETWEEN TWO NODES:")
        print("    ", end="")  # For column labels
        for col in range(len(self._nodes_matrix)):
            print(f"{self._vertices[col]} ", end=" ")
        print()
        
        for row in range(len(self._nodes_matrix)):
            print(f"{self._vertices[row]} ", end="")  # For row labels
            for col in range(len(self._nodes_matrix[row])):
                print(self._nodes_matrix[row][col], end=" ")
            print()

#-------------------------------------------------------------------------------------------------------------------------

    def weight_mat(self):
        # Check if there are no vertices or if the graph is empty
        length = self.num_vertices()
        if length == 0:
            print("No vertices in the graph.")
            return

        # Initialize matrices for weights and node identifiers
        mat = [[0 for _ in range(length)] for _ in range(length)]
        nodes = [["-" for _ in range(length)] for _ in range(length)]
        
        vertex = self._head_vertex

        # Populate the weight and node matrices based on the graph's edges
        while vertex is not None:
            parent_index = self._vertex_indices[vertex.key]
            current_edge = vertex.edge

            while current_edge is not None:
                destination_index = self._vertex_indices[current_edge.vertex.key]
                mat[parent_index][destination_index] = current_edge.value  # Store edge weight
                nodes[parent_index][destination_index] = f"{self._vertices[parent_index]}{self._vertices[destination_index]}"  # Store node identifier
                current_edge = current_edge.next

            vertex = vertex.next

        # Store the generated matrices in the instance
        self._weight_matrix = mat
        self._nodes_matrix = nodes

#------------------------------------------------------------------------------------------------------------------------

    def direct_paths(self):
        # Lists direct paths with their weights based on the weight matrix
        print("DIRECT PATHS:")
        for row in range(len(self._weight_matrix)):
            for col in range(len(self._weight_matrix)):
                if self._weight_matrix[row][col] != 0:
                    print(f"Path: {self._vertices[row]} --> {self._vertices[col]}. "
                          f"Path weight: {self._weight_matrix[row][col]}")

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def add_all_paths(arr):
        if not arr:
            return []  # Return an empty list if arr is empty
        # Initialize result as the first matrix in arr
        result = [row[:] for row in arr[0]]  # Make a deep copy of the first matrix
        
        # Iterate over remaining matrices
        for matrix in arr[1:]:
            # Check if dimensions match
            assert len(matrix) == len(result) and len(matrix[0]) == len(result[0]), "Matrices must have the same dimensions"
            # Element-wise addition
            for row in range(len(result)):
                for col in range(len(result[0])):
                    result[row][col] += matrix[row][col]
                    
        return result

#------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def matmul(mat1, mat2):
        assert len(mat1[0]) == len(mat2), "Multiplication not possible!"
        x = len(mat1)
        y = len(mat2[0])
        z = len(mat1[0])
        mat = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
        return mat

#-------------------------------------------------------------------------------------------------------------------------

    def path_mat(self):
        paths = []
        result = [row[:] for row in self._adjacency_matrix]  # Deep copy to avoid modifying the original adjacency matrix
        paths.append(result)
        length = self.num_vertices()  # Corrected method name

        for _ in range(1, length):
            result = Graph.matmul(result, self._adjacency_matrix)

            # Check if the resulting matrix is identical to the last matrix in paths
            if result == paths[-1]:
                break

            # Check if all elements in result are zero
            if all(result[row][col] == 0 for row in range(len(result)) for col in range(len(result[0]))):
                break

            paths.append(result)

        # Summing all path matrices to form the path matrix
        path_matrix = Graph.add_all_paths(paths)
        self._path_matrix = path_matrix

#-------------------------------------------------------------------------------------------------------------------------

    def print_all_paths(self):
        if not self._path_matrix:
            print("Path matrix is empty. No paths available.")
            return

        print("ALL POSSIBLE PATHS:")

        for row in range(len(self._path_matrix)):
            print(f"\nPaths from {self._vertices[row]}:")
            has_paths = False
            for col in range(len(self._path_matrix[row])):
                paths = self._path_matrix[row][col]
                if paths > 0:
                    print(f"  {self._vertices[row]} --> {self._vertices[col]} : {paths} Possible path(s)")
                    has_paths = True
            if not has_paths:
                print("  No paths available.")

#------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def change_state(mat1, mat2, fixed):
        for row in range(len(mat1)):
            for col in range(len(mat1)):
                if row == fixed or col == fixed:
                    continue
                
                ans = mat1[fixed][col] + mat1[row][fixed]
                if ans < mat1[row][col]:
                    mat1[row][col] = ans

                    # Concatenate paths with reduced redundancy
                    str1 = mat2[row][fixed]# Ensure str1 has at least `fixed`
                    str2 = mat2[fixed][col]# Ensure str2 has at least `fixed`
                    mat2[row][fixed]
                    # Avoid overlapping segments
                    if str1[-1] == str2[0]:
                        mat2[row][col] = str1 + str2[1:]
                    else:
                        mat2[row][col] = str1 + str2

#-------------------------------------------------------------------------------------------------------------------------

    def spa(self):
        # Initialize the shortest path matrices
        shortest_path = [row[:] for row in self._weight_matrix]
        shortest_path_nodes = [[str(i) for i in row] for row in self._nodes_matrix]  # Ensure node paths are strings

        # Replace 0s with infinity except on the diagonal
        for row in range(len(shortest_path)):
            for col in range(len(shortest_path[row])):
                if shortest_path[row][col] == 0:
                    shortest_path[row][col] = float('inf')

        # Update shortest path using change_state method
        for i in range(len(self._vertices)):
            Graph.change_state(shortest_path, shortest_path_nodes, i)

        # Store the final matrices
        self._shortest_paths = shortest_path
        self._shortest_path_nodes = shortest_path_nodes

# #-------------------------------------------------------------------------------------------------------------------------

    def display_shortest_paths(self):
        print("SHORTEST PATHS BETWEEN NODES:")
        for row in range(len(self._shortest_paths)):
            for col in range(len(self._shortest_paths[row])):
                # Skip if there's no path (infinity weight)
                if self._shortest_paths[row][col] == float('inf'):
                    continue
                # Get the path and weight
                path = self._shortest_path_nodes[row][col]
                weight = self._shortest_paths[row][col]
                print(f"{self._vertices[row]} --> {self._vertices[col]} : Path = {path}, Weight = {weight}")

#-------------------------------------------------------------------------------------------------------------------------

    def make_adj_table(self):
        table = {vertex : [() ,1] for vertex in self._vertices}

        for row in range(len(self._adjacency_matrix)):
            for col in range(len(self._adjacency_matrix)):

                if self._adjacency_matrix[row][col] == 1:
                    table[self._vertices[row]][0] += (self._vertices[col],)

        self._adjacency_table = table

#-------------------------------------------------------------------------------------------------------------------------

    def print_adj_table(self):
        print(f"{'VERTICES':<15}{'NEIGHBOURS':<30}{'STATUS':<10}")
        print("-" * 55)  # Add a line separator for clarity

        # Iterate over the adjacency table and print the details
        for key, value in self._adjacency_table.items():
            neighbors = ', '.join(value[0])  # Join the list of neighbors into a string
            status = value[1]
            
            # Format the output neatly
            print(f"{key:<15}{neighbors:<30}{status:<10}")

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def make_path(arr1, arr2, start, target):
        path = []
        index = -1

        for idx in range(len(arr1) - 1, -1, -1):
            if arr1[idx] == target:
                index = idx
                break

        if index == -1:
            return []

        current = index
        while current != -1:
            path.append(arr1[current])
            if arr1[current] == start: 
                break

            parent = arr2[current]
            if parent is None:  
                break
            try:
                current = arr1.index(parent)  
            except ValueError:
                return []

        return path[::-1]

#-------------------------------------------------------------------------------------------------------------------------

    def bfs(self ,start ,end):
        q = [start]
        o = [None]
        self._adjacency_table[start][1] = 2
        front ,rear = 0 ,0

        while front <= rear and end not in q:
            temp = q[front]
            front += 1
            self._adjacency_table[temp][1] = 3
            neighbours = [item for item in self._adjacency_table[temp][0] if item not in q]
            num_neighbours = [temp for _ in range(len(neighbours))]
            o.extend(num_neighbours)
            q.extend(neighbours)

            for key in self._adjacency_table.keys():
                if key in neighbours:
                    self._adjacency_table[key][1] += 2

            rear += len(neighbours)

        path = Graph.make_path(q ,o ,start ,end)
        return "-->".join(path)

#-------------------------------------------------------------------------------------------------------------------------

    def dfs(self ,start):
        path = []
        stack = [start]
        self._adjacency_table[start][1] = 2

        while stack != []:
            node = stack.pop()
            self._adjacency_table[node][1] = 3
            path.append(node)
            neighbours = [item for item in self._adjacency_table[node][0] if item not in stack and item not in path]
            stack.extend(neighbours)
            for neighbour in neighbours:
                self._adjacency_table[neighbour][1] = 2
        
        return "-->".join(path)

#-------------------------------------------------------------------------------------------------------------------------

# Test the Graph functionality
# g1 = Graph(["A", "H", "B", "C", "M", "D", "R"])

# g1.add_edge((103, "A", "H"))
# g1.add_edge((106, "H", "A"))
# g1.add_edge((201, "B", "C"))
# g1.add_edge((203, "B", "D"))
# g1.add_edge((305, "C", "M"))
# g1.add_edge((308, "M", "B"))
# g1.add_edge((204, "D", "B"))
# g1.add_edge((301, "D", "R"))
# g1.add_edge((402, "R", "C"))
# g1.adj_mat()
# g1.weight_mat()
# g1.path_mat()
# g1.spa()
# g1.make_adj_table()
# g1.print_adj_table()
# ####################
# g1.print_graph()
# g1.print_adj()
# g1.print_nodes_mat()
# g1.direct_paths()
# g1.print_all_paths()
# g1.display_shortest_paths()

#=========================================================================================================================
