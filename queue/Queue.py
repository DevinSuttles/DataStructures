class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
class Queue:
    def __init__(self):
        self.que=Node()
    def isEmpty(self):
        return self.que==None
    def enqueue(self,value):
        if self.isEmpty():
            self.que.data=value   
        temp=self.que
        while temp.next!= None:
            temp=temp.next
        temp2=Node()
        temp2.data=value
        temp.next=temp2 
    def peek(self):
        return self.que.data
obj=Queue()
print(obj.isEmpty())
obj.enqueue(100)
obj.enqueue(88)
obj.enqueue(99999)
obj.enqueue(8)
print(obj.peek())
