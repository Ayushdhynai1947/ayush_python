class node:
    def __init__(self,item = None ,data = None,right = None) -> None:
        self.left = None
        self.data = None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self,data):
        self.root = self.rinsert(self.root ,data)
        
    def rinsert(self,root,data):
        if root is None:
            return node(data)
        if data <root.item:
            root.left = self.rinsert(root.left ,data)
        elif data >root.item :
            root.right = self.rinsert(root.right,data)
        return root








