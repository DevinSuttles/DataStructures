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
        return self._height(self.root)
    def _height(self,root):
        if root==None:
            return 0
        else:
            return 1+max(self._height(root.leftChild),self._height(root.rightChild))
    def numberOfNodes(self):
        return self._numberOfNodes(self.root)
    def _numberOfNodes(self,root):
        if root==None:
            return 0
        else:
            return 1+self._numberOfNodes(root.leftChild)+self._numberOfNodes(root.rightChild)
    def find(self,value):
        return self._find(self,self.root,value)!=None
    def _find(self,root,value):
        if root==None:
            return None
        elif value<root.data:
            self._find(root.leftChild,value)
        elif value>root.data:
            self._find(root.rightChild,value)
        elif root.data==value:
            return root
