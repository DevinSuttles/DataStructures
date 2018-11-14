class BinaryNode:
    def __init__(self):
        self.rightChild=None
        self.leftChild=None
        self.data=None
class BinarySearchTree:
    def __init__(self,value):
        self.root=BinaryNode()
        self.root.data=value
    def isEmpty(self):
        return self.root==None
    def height(self):
        if self.isEmpty():
            raise Exception("No value in binary tree so height is zero.")
        return self._height(self.root)
    def _height(self,root):
        if root==None:
            return 0
        else:
            return 1+self._height(root.leftChild)+self._height(root.rightChild)
