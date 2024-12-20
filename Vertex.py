class Vertex:
    def __init__(self ,key):
        self.key = key
        self.next = None
        self.edge = None

    def __str__(self):
        return f"| {self.key} | . | -|-->"