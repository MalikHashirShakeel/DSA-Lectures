#-----------------------------------------------------------------------------------------------
# Binary Search Tree Implementation with Full Documentation
#-----------------------------------------------------------------------------------------------

class TreeNode:
    """
    A class representing a single node in a binary search tree (BST).
    Each node contains a value, a reference to a left child, and a right child.
    """

    def __init__(self, value):
        """
        Initialize a TreeNode with a given value.
        :param value: The value of the node.
        """
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        """
        Add a new value to the BST while maintaining BST properties.
        :param value: The value to add to the tree.
        """
        if value < self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.add(value)
        elif value > self.value:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.add(value)

    def left_logical_successor(self):
        """
        Find the left-most logical successor in the subtree rooted at this node.
        :return: The left-most logical successor.
        """
        current = self
        while current.left:
            current = current.left
        return current

    def right_logical_successor(self):
        """
        Find the right-most logical successor in the subtree rooted at this node.
        :return: The right-most logical successor.
        """
        current = self
        while current.right:
            current = current.right
        return current

    def parse_tree(self, lst=None):
        """
        Traverse the BST in in-order and collect the values in a list.
        :param lst: The list to store values (used for recursion).
        :return: The list of values in sorted order.
        """
        if lst is None:
            lst = []

        if self.left:
            self.left.parse_tree(lst)

        lst.append(self.value)

        if self.right:
            self.right.parse_tree(lst)

        return lst

    def search(self, value, parent=None):
        """
        Search for a node with the specified value in the BST.
        :param value: The value to search for.
        :param parent: The parent of the current node (used for deletion).
        :return: A tuple containing the node and its parent, or (None, None) if not found.
        """
        if self.value == value:
            return [self, parent]

        if value < self.value and self.left:
            return self.left.search(value, self)

        if value > self.value and self.right:
            return self.right.search(value, self)

        return [None, None]

    def delete(self, value):
        """
        Delete a node with the specified value from the BST.
        :param value: The value to delete.
        """
        node, parent = self.search(value)

        if node is None:
            raise Exception("Node not found in the tree.")

        # Case 1: Node has no children (leaf node)
        if not node.left and not node.right:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                raise Exception("Cannot delete the root node without children.")

        # Case 2: Node has one child
        elif not node.left or not node.right:
            child = node.left if node.left else node.right
            if parent:
                if parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
            else:
                # Replace root node
                node.value = child.value
                node.left = child.left
                node.right = child.right

        # Case 3: Node has two children
        else:
            # Find the in-order successor (smallest value in the right subtree)
            successor = node.right.left_logical_successor()
            node.value = successor.value
            # Delete the successor node
            node.right.delete(successor.value)

#-----------------------------------------------------------------------------------------------
# Helper Functions
#-----------------------------------------------------------------------------------------------

def build_bst(lst):
    """
    Build a binary search tree (BST) from a list of values.
    :param lst: A list of values to add to the BST.
    :return: The root node of the constructed BST.
    """
    if not lst:
        raise ValueError("Input list is empty.")

    root = TreeNode(lst[0])

    for value in lst[1:]:
        root.add(value)

    return root

#-----------------------------------------------------------------------------------------------
