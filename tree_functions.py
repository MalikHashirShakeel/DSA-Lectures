from Binary_Search_Tree import TreeNode

def build_tree(arr):
    if len(arr) == 0 or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    nodes = [root]  # To keep track of tree nodes
    nodes_idx = 0  # Tracks the index of the parent node in `nodes`
    root_idx = 1  # Tracks the index in `arr` where child nodes are located

    while root_idx < len(arr):
        # Add left child if applicable
        if root_idx < len(arr) and arr[root_idx] is not None:
            nodes[nodes_idx].left = TreeNode(arr[root_idx])
            nodes.append(nodes[nodes_idx].left)
        root_idx += 1

        # Add right child if applicable
        if root_idx < len(arr) and arr[root_idx] is not None:
            nodes[nodes_idx].right = TreeNode(arr[root_idx])
            nodes.append(nodes[nodes_idx].right)
        root_idx += 1

        # Move to the next node in `nodes`
        nodes_idx += 1

    return root

#-------------------------------------------------------------------------------------------------------------------------

def search(node ,target):
    if node is None:
        return None
    
    if node.value == target:
        return node
    
    if not node.left and not node.right:
        return None
    
    left = search(node.left ,target)
    if left:
        return left
    right = search(node.right ,target)
    if right:
        return right
    
    return None

#-------------------------------------------------------------------------------------------------------------------------

# arr = [1, 2, 3, 4, 5, None, 7]
# root = build_tree(arr)
# print(root.right.value)