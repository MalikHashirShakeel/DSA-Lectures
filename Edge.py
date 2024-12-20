class Edge:
    def __init__(self ,value):
        self.vertex = None
        self.value = value
        self.next = None
        
    def __str__(self):
        # Return the format with the vertex key and edge value
        return f"| {self.vertex.key} | {self.value} | |--> "