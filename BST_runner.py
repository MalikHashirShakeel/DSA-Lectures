from BST import *

root = TreeNode(10)
root.add(5)
root.add(15)
root.add(8)
# print(root.right.value)
# print(root.left.value)
# print(root.left.right.value)

# The BST structure is now:
#       10
#      /  \
#     5   15
#      \
#       8

# print(root.left.left_logical_successor())
# print(root.right.right_logical_successor())
# print(root.parse_tree())
lst = root.search(8)
# print(lst[0].value ,lst[1].value)
root.delete(8)
