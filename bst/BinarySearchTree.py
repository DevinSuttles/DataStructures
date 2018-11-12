class BinaryNode:
    def __init__(self):
        self.right=None
        self.left=None
        self.data=None
class BinarySearchTree:
    def __init__(self,value):
        self.m_root=BinaryNode()
        self.m_root.data=value
