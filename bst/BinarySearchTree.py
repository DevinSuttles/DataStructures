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
            return rSearch(self,root.rightNode,value)
        else
            return rSearch(self,root.leftNode,value)
