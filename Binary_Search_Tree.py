class TreeNode:
    def __init__(self, value, left=None, right=None):
        """
        Initialize a Node with a value, and optionally left and right children.
        """
        self.value = value  # Store the value of the node
        self.left = left    # Reference to the left child (default: None)
        self.right = right  # Reference to the right child (default: None)

#-------------------------------------------------------------------------------------------------------------------------

    def add_left_child(self ,val):
        assert not self.left ,"Left child already present."
        self.left = TreeNode(val)

#-------------------------------------------------------------------------------------------------------------------------

    def add_right_child(self ,val):
        assert not self.right ,"Right child already present."
        self.right = TreeNode(val)

#-------------------------------------------------------------------------------------------------------------------------

    def delete_left(self):
        assert self.left is not None ,"Child does not exists."
        assert not self.left.left and not self.left.right ,"The given node contains children."

        value = self.left.data 
        self.left = None
        return value
    
#-------------------------------------------------------------------------------------------------------------------------

    def delete_right(self):
        assert self.right is not None ,"Child does not exists."
        assert not self.right.left and not self.right.right ,"The given node contains children."

        value = self.right.data
        self.right = None
        return value
    
#-------------------------------------------------------------------------------------------------------------------------

    def height(self):
        """
        Calculate the height of the tree.
        Height is defined as the number of levels in the tree.
        """
        if self is None:
            return 0  # An empty tree has a height of 0

        # Recursively calculate the height of left and right subtrees
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        # Height of the current tree is 1 (for the current node) + the max of subtree heights
        return 1 + max(left_height, right_height)
    
#-------------------------------------------------------------------------------------------------------------------------

    def node_count(self):
        """
        Calculate the total number of nodes in the tree.
        """
        if self is None:
            return 0  # An empty tree has 0 nodes

        # Recursively count nodes in left and right subtrees
        left_count = self.left.node_count() if self.left else 0
        right_count = self.right.node_count() if self.right else 0

        # Total nodes include the current node (1) + left + right counts
        return 1 + left_count + right_count
    
#-------------------------------------------------------------------------------------------------------------------------

    def edge_count(self):
        return self.node_count() - 1
    
#-------------------------------------------------------------------------------------------------------------------------

    def leaf_count(self):
        if not self.left and not self.right:
            return 1
        
        left_leaf_count = self.left.leaf_count() if self.left else 0
        right_leaf_count = self.right.leaf_count() if self.right else 0

        return left_leaf_count + right_leaf_count

#-------------------------------------------------------------------------------------------------------------------------

    def is_strictly_binary_tree(self):
        if self is None:
            return True
        
        if not self.left and not self.right:
            return True
        
        elif not self.left or not self.right:
            return False
        
        else:
            return self.left.is_strictly_binary_tree() and self.right.is_strictly_binary_tree()
        
#-------------------------------------------------------------------------------------------------------------------------

    def is_perfect_binary_tree(self):
        """
        Check if the tree is a perfect binary tree.
        A perfect binary tree has all internal nodes with two children,
        and all leaves are at the same level.
        """
        # Calculate the height of the tree
        height = self.height()

        # Calculate the total number of nodes in the tree
        nodes = self.node_count()

        # A perfect binary tree of height h has 2^h - 1 nodes
        pbt_nodes = 2 ** height - 1

        # Check if the current number of nodes matches the expected nodes
        return nodes == pbt_nodes

#-------------------------------------------------------------------------------------------------------------------------

    def is_ACBT(self):
        # If the tree is perfect, it is automatically an ACBT
        if self.is_perfect_binary_tree():
            return True

        # A node with a right child but no left child violates ACBT property
        if self.right and not self.left:
            return False

        # Calculate heights of left and right subtrees
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0

        # Height difference must be 0 or 1
        if left_height - right_height not in (0, 1):
            return False

        # Check subtrees recursively
        if left_height == right_height:
            return self.left.is_perfect_binary_tree() and self.right.is_ACBT()

        return self.left.is_ACBT()
    
#-------------------------------------------------------------------------------------------------------------------------

    def traversal_inorder(self):
        if self.left:
            self.left.traversal_inorder()

        print(self.value ,end = " ")

        if self.right:
            self.right.traversal_inorder()

#-------------------------------------------------------------------------------------------------------------------------

    def traversal_preorder(self):
            print(self.value ,end = " ")

            if self.left:
                self.left.traversal_preorder()

            if self.right:
                self.right.traversal_preorder()

#-------------------------------------------------------------------------------------------------------------------------

    def traversal_postorder(self):
            if self.left:
                self.left.traversal_postorder()

            if self.right:
                self.right.traversal_postorder()

            print(self.value ,end = " ")

#-------------------------------------------------------------------------------------------------------------------------

    def double_order_traversal(self):
        if self is None:
            return
        
        # Visit the node (first time)
        print(self.value, end=" ")

        # Traverse the left subtree
        if self.left:
            self.left.double_order_traversal()

        # Visit the node (second time)
        print(self.value, end=" ")

        # Traverse the right subtree
        if self.right:
            self.right.double_order_traversal()

#-------------------------------------------------------------------------------------------------------------------------

    def traversal_bf(self):
        if self is None:
            return None
        
        queue = [self]

        while queue != []:
            node = queue.pop(0)
            print(node.value, end = " ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

#-------------------------------------------------------------------------------------------------------------------------

    def traversal_df(self):
        if self is None:
            return None
        
        stack = [self]

        while stack != []:
            node = stack.pop()
            print(node.value, end = " ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

#-------------------------------------------------------------------------------------------------------------------------

    def clear_tree(self):
        if self is None:
            return
        
        # Traverse the left subtree
        if self.left:
            self.left.clear_tree()

        # Traverse the right subtree
        if self.right:
            self.right.clear_tree()

        # Clear the current node
        self.value = 0

#=========================================================================================================================
#FUNCTIONS

def build(val):
    assert len(val) > 0 and val[0] != None ,"Invalid input."
    nodes = [val[0]]
    root = val[0]
    n = 0
    i = 1

    while i < len(val):
        p = nodes[n]
        if val[i]:
            p.add_left_child(val[i])
            nodes.append(val[i])
        i += 1

        if val[i]:
            p.add_right_child(val[i])
            nodes.append(val[i])
        i += 1
        n += 1

    return root
    
        


