#-----------------------------------------------------------------------------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#-----------------------------------------------------------------------------------------------

    def add(self, value):
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

#----------------------------------------------------------------------------------------------

    def left_logical_successor(self):
        if self is None:
            return None
        
        if not self.right:
            return self

        return self.right.left_logical_successor()

#-----------------------------------------------------------------------------------------------

    def right_logical_successor(self):
        if self is None:
            return None

        if not self.left:
            return self

        return self.left.right_logical_successor()

#-----------------------------------------------------------------------------------------------

    def parse_tree(self, lst=None):
        if lst is None:
            lst = []  

        if self.left:
            self.left.parse_tree(lst)

        lst.append(self.value)

        if self.right:
            self.right.parse_tree(lst)

        return lst
#-----------------------------------------------------------------------------------------------

    def search(self, value, parent=None):

        if self.value == value:
            return [self, parent]

        if value < self.value and self.left:
            return self.left.search(value, self)

        if value > self.value and self.right:
            return self.right.search(value, self)

        return [None, None]
    
#-----------------------------------------------------------------------------------------------

    def delete(self ,value):
        nodes = self.search(value)

        if nodes == [None ,None]:
            raise Exception("Node not found in the tree.")
        
        elif not nodes[0].left and not nodes[0].right:
            nodes[1].left = None if nodes[1].left == nodes[0] else nodes[1].right = None

        elif not nodes[0].left or not nodes[0].right:

            if nodes[0].left:
                nodes[1].left = nodes[0].left if nodes[1].left == nodes[0] else nodes[1].right = nodes[0].left
            else:
                nodes[1].left = nodes[0].right if nodes[1].left == nodes[0] else nodes[1].right = nodes[0].right

        else:
            successor = nodes[0].right.right_logical_successor()
            nodes[0].value = successor.value
            if successor.right:
                successor.value = successor.right.value
                successor.right = successor.right.right
            else:
                del(successor)

#-----------------------------------------------------------------------------------------------

#===============================================================================================
#FUNCTIONS

def build_bst(lst):
    root = TreeNode(lst[0])

    for node_idx in range(len(lst)):
        root.add(lst[node_idx])

    return root

#-----------------------------------------------------------------------------------------------


    