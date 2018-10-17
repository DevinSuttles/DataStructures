class BinaryNode:
    def __init__(self):
        self.rightNode=None
        self.leftNode=None
        self.data=None
class BinarySearchTree:
    def __init__(self):
        self.m_root=BinaryNode()
    def search(self,find):
        root=self.m_root
        return rSearch(self,root,find)
    def rSearch(self,root,value):
        if root.data==value:
            return True
        else if root.data>value:
            return self.rSearch(root.leftNode,value)
        else
            return self.rSearch(root.rightNode,value)
    def add(self,value):
        root=self.m_root
        return self.insert(root,value)
    def insert(self,root,value):
        if root==None:
            root.data=value
        else if root.data>value:
            self.insert(root.left,value)
        else:
            self.insert(root.right,value)
    def postOrder(self,root):
        if root!=None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)
