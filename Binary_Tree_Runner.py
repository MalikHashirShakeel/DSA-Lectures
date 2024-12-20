from Binary_Search_Tree import TreeNode
from tree_functions import *

# Create a test binary tree
# Example of a perfect binary tree:
#       1
#      / \
#     2   3
#    / \ / \
#   4  5 6  7

root = TreeNode(1)  # Root node
root.left = TreeNode(2, TreeNode(4), TreeNode(5))  # Left subtree
root.right = TreeNode(3, TreeNode(6), TreeNode(7))  # Right subtree

# Test the methods
print("Tree Height:", root.height())  # Should output: 3
print("Total Node Count:", root.node_count())  # Should output: 7
print('Total Leaves are:' ,root.leaf_count())
print("Is strictly binary tree:" ,root.is_strictly_binary_tree())
print("Is Perfect Binary Tree:", root.is_perfect_binary_tree())  # Should output: True
print("Double Order traversal:", root.double_order_traversal())
print("In Order traversal:", root.traversal_inorder())
print("Breadth first traversal:", root.traversal_bf())
root.traversal_df()
print()
obj = search(root ,8)
print(obj.value if obj else None)
# print(root.is_ACBT())
# root.clear_tree()
# root.double_order_traversal()
# Modify the tree to test for imperfection
# Remove a node to make it imperfect
root.right.right = None

print("\nAfter Modification:")
print("Tree Height:", root.height())  # Should output: 3
print("Total Node Count:", root.node_count())  # Should output: 6
print('Total Leaves are:' ,root.leaf_count())
print("Is strictly binary tree:" ,root.is_strictly_binary_tree())
print("Is Perfect Binary Tree:", root.is_perfect_binary_tree())  # Should output: False
print(root.is_ACBT())
