class node:
    def __init__(self, item = None ,right = None,left=None) -> None:
        self.item = item 
        self.left = left
        self.right = right
        
    
class BST:
    def __init__(self) -> None:
        self.root = None
        self.item_count = 0
        
        
    def insert(self,data):
        self.root = self.rinsert(self.root ,data)
        
    def rinsert(self,root ,data):
        if root is None:
            return node(data)
        if data<root.item:
            root.left = self.rinsert(root.left,data)
            
        elif data>root.item:
            root.right = self.rinsert(root.right,data)
        return root       
    def search(self,data):
        return self.rsearch(self.root,data)
    def rsearch(self,root ,data):
        if root is None or root.item ==data:
            return root
        if data<root.item:
            return self.rsearch(root.left ,data)
        else:
            return self.rsearch(root.right,data)
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)
            
    def preorder(self):
        result = []
        self.rpreorder(self.root,result)
        return result
    
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left ,result)
            self.rpreorder(root.right,result)
        
    def postorder(self):
        result = []
        self.rpostorder(self.root,result)
        return result
    
    def rpostorder(self,root,result):
        if root:
           
            self.rpostorder(root.left ,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
            
    
    def min_value(self,temp):
        current = temp
        while current.left is not None:
            current = current.left
            
        return current.item
    
    def max_value(self,temp):
        current = temp
        while current.right is not None:
            current= current.right
        return current.item
    
    def delete(self,data):
        self.root = self.rdelete(self.root,data)
        
    def rdelete(self,root,data):
        if root is None:
            return root
        if data < root.item:
            root.left =self.rdelete(root.left,data)
        elif data > root.item:
            root.right =self.rdelete(root.right ,data)
        
        else:
            if  root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item  = self.min_value(root.right)
            self.rdelete(root.right,root.item)
        
        return root
    def size(self):
        return len(self.inorder())
    
    


# Creating an instance of the BST class
bst = BST()

# Inserting elements into the BST
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

# Printing the inorder traversal of the BST
print("Inorder Traversal:", bst.inorder())

# Performing some operations on the BST
print("Size of BST:", bst.size())
print("Min value:", bst.min_value(bst.root))
print("Max value:", bst.max_value(bst.root))

# Searching for elements in the BST
print("Searching for 40:", bst.search(40))
print("Searching for 90:", bst.search(90))

# Deleting elements from the BST
bst.delete(30)
print("Inorder Traversal after deleting 30:", bst.inorder())

bst.delete(50)
print("Inorder Traversal after deleting 50:", bst.inorder())

    