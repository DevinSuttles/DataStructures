class MaxHeap(object):
    def __init__(self):
        self.list=[]
        self.size=0
    def insert(self,value):
        self.list.append(value)
        self.size+=1
    def getSize(self):
        return self.size
