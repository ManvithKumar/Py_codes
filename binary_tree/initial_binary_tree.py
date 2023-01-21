class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        

class Binary_tree:
    def __init__(self,root):
        self.root=Node(root)


tree=Binary_tree(34)
tree.root.left=Node(33)
tree.root.right=Node(45)
