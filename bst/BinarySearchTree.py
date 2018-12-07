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
    def insert(self,value):
        if self.root==None:
            self.root=BinaryNode()
            self.root.data=value
        else:
            self._insert(self.root,value)
    def _insert(self,root,value):
        if value>root.data:
            if root.rightChild==None:
                temp=BinaryNode()
                temp.data=value
                root.rightChild=temp
            else:
                self._insert(root.rightChild,value)
        if value<root.data:
            if root.leftChild==None:
                temp=BinaryNode()
                temp.data=value
                root.leftChild=temp
            else:
                self._insert(root.leftChild,value)
        if value==root.data:
            raise Exception("No duplicate values allowed in bst.")
    def _inorder(self,root):
        if root!=None:
            self._inorder(root.leftChild)
            print(root.data)
            self._inorder(root.rightChild)
    def inorder(self):
        self._inorder(self.root)
    def _preorder(self,root):
        if root!=None:
            print(root.data)
            self._preorder(root.leftChild)
            self._preorder(root.rightChild)
    def preorder(self):
        self._preorder(self.root)
    def _postorder(self,root):
        if root!=None:
            self._postorder(root.leftChild)
            self._postorder(root.rightChild)
            print(root.data)
    def postorder(self):
        self._postorder(self.root)
    def delete(self,value):
        root=self.root
        if root==None:
            raise Exception("Nothing to delte")
