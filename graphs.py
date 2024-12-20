from queue_simple import Queue

class Graph:
    def __init__(self, vertices, edges):
        # Initialize a graph with a specified number of vertices and edges.
        
        self._vertices = vertices  # Number of vertices in the graph.
        
        # Initialize an adjacency list, where each vertex has a list of connected vertices.
        self._data = [[] for _ in range(self._vertices)]  # Create an empty adjacency list for each vertex.
        
        # Add edges to the graph. Each edge connects two vertices (item1 and item2).
        for item1, item2 in edges:
            self._data[item1].append(item2)  # Append item2 to the adjacency list of item1.
            self._data[item2].append(item1)  # Append item1 to the adjacency list of item2 (since this is an undirected graph).
#-------------------------------------------------------------------------------------------------------------------------

    def __repr__(self):
        # Return a string representation of the graph's adjacency list.
        s = ''
        # Iterate through each vertex and its adjacency list.
        for idx, item in enumerate(self._data):
            # Format the adjacency list of each vertex as a string.
            s += f"| {idx} | -> | {' | '.join(map(str, item))} |\n"
        # Return the formatted string, or a message if there is no data.
        return s if s else "No data available."

#-------------------------------------------------------------------------------------------------------------------------

    def __str__(self):
        # Return the string representation of the graph.
        return self.__repr__()

#-------------------------------------------------------------------------------------------------------------------------

    def breadth_first_search(self, root):
        bfs_elements = []
        queue = Queue()
        visited = [False for _ in range(len(self._data))]  # Initialize visited list
        
        queue.enqueue(root)  # Enqueue the root node index (integer), not its data
        visited[root] = True  # Mark root as visited
        bfs_elements.append(root)  # Add root to the result list
        
        while not queue.is_empty():
            current = queue.dequeue()  # Dequeue the current node index (integer)
            
            for node in self._data[current]:  # Iterate over neighbors of the current node
                if not visited[node]:  # If neighbor hasn't been visited
                    queue.enqueue(node)  # Enqueue the neighbor index
                    visited[node] = True  # Mark the neighbor as visited
                    bfs_elements.append(node)  # Append neighbor to result list
        
        return bfs_elements

#=========================================================================================================================

vertices = 5
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 4)]
g1 = Graph(vertices, edges)
print(g1)
print(g1.breadth_first_search(3))