import math
class MaxHeap(object):

    def __init__(self):
        self.list=[]
        self.count=-1


    def push(self,value):
        self.count=self.count+1
        self.list.append(value)
        self._downHeap(self.count)


    def peek(self):
        if self.count != -1:
            return self.list[0]


    def _swap(self, i , j):
        self.list[i],self.list[j]=self.list[j],self.list[i]

    def buildHeap(self):
        self._upHeap(self.count)


    def levelOrder(self):
        for i in self.list:
            print(i,end=" ")


    def _downHeap(self,index):
        parent=math.floor((index-1)/2)
        print(parent)
        if self.list[parent]<self.list[index]:
            self._swap(index,parent)
