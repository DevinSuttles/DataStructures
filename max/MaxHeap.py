class MaxHeap(object):

    def __init__(self):
        self.list=[]

#adds to the max heap
    def push(self,value):
        self.list.append(value)
        self._upHeap(len(self.list)-1)

#gives back the MaxValue
    def peek(self):
        if self.size != 0:
            return self.list[1]

#swap
    def _swap(self, i , j):
        self.list[i],self.list[j]=self.list[j],self.list[i]

#upheap
    def _upHeap(self,i):
        parent=i//2
        if i <=1:
            return
        elif self.list[i] > self.list[parent]:
            self._swap(i,parent)
            self._upHeap(parent)
