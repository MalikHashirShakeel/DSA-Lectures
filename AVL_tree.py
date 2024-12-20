class AVL:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

#-------------------------------------------------------------------------------------------------------------------------
    
    def height(self):
        """
        Calculate the height of the tree rooted at this node.
        The height is the number of edges on the longest path from the node to a leaf.
        """
        left_height = self._get_child_height(self.left)
        right_height = self._get_child_height(self.right)
        return 1 + max(left_height, right_height)

    def _get_child_height(self, child):
        """Returns the height of a child node or 0 if the child is None."""
        return child.height() if child else 0

#-------------------------------------------------------------------------------------------------------------------------
    
    def is_balanced(self):
        """
        Check if the node is balanced.
        A node is balanced if the difference in height between its left and right subtrees is <= 1.
        """
        left_height = self._get_child_height(self.left)
        right_height = self._get_child_height(self.right)
        return abs(left_height - right_height) <= 1
    
#-------------------------------------------------------------------------------------------------------------------------

    def find_unstability(self, node):
        """
        Traverse upwards from the node to find the first unbalanced node.
        """
        curr = node
        if not curr.is_balanced():
            return curr
        while curr and curr.is_balanced():
            curr = curr.parent
        return curr  

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def update_parent(parent, old_child, new_child):
        """
        Update the parent-child relationship after rotation.
        This method ensures that the parent now points to the new child after rotation.
        """
        if parent:
            if parent.left == old_child:
                parent.left = new_child
            else:
                parent.right = new_child

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def right_rotation(a, b):
        """
        Perform a right rotation on the tree with nodes a and b.
        This will adjust the parent-child relationships accordingly.
        """
        # Update parent relationships
        b.parent = a.parent
        a.parent = b

        if b.right:
            b.right.parent = a
        a.right = b.right

        b.right = a
        AVL.update_parent(b.parent, a, b)

#-------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def left_rotation(a, b):
        """
        Perform a left rotation on the tree with nodes a and b.
        This will adjust the parent-child relationships accordingly.
        """
        # Update parent relationships
        b.parent = a.parent
        a.parent = b

        if b.left:
            b.left.parent = a
        a.left = b.left

        b.left = a
        AVL.update_parent(b.parent, a, b)

#------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def rotate(a, b, p1, p2):
        """
        Determine which type of rotation to perform based on the position of a and b.
        The rotations can be left or right depending on the imbalance pattern.
        """
        if (p1, p2) == ("l", "l"):
            AVL.right_rotation(a, b)
        elif (p1, p2) == ("r", "r"):
            AVL.left_rotation(a, b)
        elif (p1, p2) == ("l", "r"):
            AVL.left_rotation(b, b.right)
            AVL.right_rotation(a, a.left)
        elif (p1, p2) == ("r", "l"):
            AVL.right_rotation(b, b.left)
            AVL.left_rotation(a, a.right)

#-------------------------------------------------------------------------------------------------------------------------

    def balance_tree(self, node):
        """
        Balance the tree starting from the given node.
        If any node is unbalanced, perform the appropriate rotations to restore balance.
        """
        a = self.find_unstability(node)

        if a:
            p1 = self._determine_position(a, node)
            p2 = self._determine_position_for_subtree(a, node, p1)

            b = a.left if p1 == "l" else a.right
            AVL.rotate(a, b, p1, p2)

#-------------------------------------------------------------------------------------------------------------------------

    def _determine_position(self, a, node):
        """
        Helper method to determine whether the imbalance is on the left or right of node a.
        """
        return "l" if a.left and node in self.get_descendants(a.left) else "r"

    def _determine_position_for_subtree(self, a, node, p1):
        """
        Helper method to determine the position for subtree b in the imbalance pattern.
        """
        return "l" if getattr(a, p1) and node in self.get_descendants(getattr(a, p1).left) else "r"

#-------------------------------------------------------------------------------------------------------------------------

    def get_descendants(self, node):
        """
        Get all descendants of a given node. This method performs a depth-first search.
        """
        descendants = set()

        def dfs(current):
            if not current:
                return
            descendants.add(current)
            dfs(current.left)
            dfs(current.right)

        dfs(node)
        return descendants
    
#-------------------------------------------------------------------------------------------------------------------------

    def insert(self, value):
        """
        Insert a value into the AVL tree. Ensure that the tree remains balanced after insertion.
        """
        if value < self.value:
            if not self.left:
                node = AVL(value)
                self.left = node
                self.left.parent = self
            else:
                node = self.left.insert(value)  
        elif value > self.value:
            if not self.right:
                node = AVL(value)
                self.right = node
                self.right.parent = self
            else:
                node = self.right.insert(value)  

        self.balance_tree(node)
        return node 
    
#-------------------------------------------------------------------------------------------------------------------------

    def parse_tree(self, lst=None):
        if lst is None:
            lst = []  

        if self.left:
            self.left.parse_tree(lst)

        lst.append(self.value)

        if self.right:
            self.right.parse_tree(lst)

        return lst
    
#-------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------

#FUNCTIONS
def build_tree(lst):
    if not lst:
        return None
    
    root = AVL(lst[0])

    for value in lst[1:]:
        root.insert(value)

    return root

#=========================================================================================================================

root = build_tree(["S" ,"P" ,"E" ,"C" ,"I" ,"A" ,"L" ,"T" ,"Y"])
root.parse_tree()