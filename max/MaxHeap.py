class MaxHeap(object):

    def __init__(self):
        self.list=[]
        self.size=-1

    def push(self,value):
        self.list.append(value)
        self.size+=1
        if self.size!=0:

#returns the size of the heap
    def getSize(self):
        return self.size

#gives back the MaxValue
    def peek(self):
        if self.size != -1:
            return self.list[0]

max=MaxHeap()
