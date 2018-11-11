class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
class Queue:
    def __init__(self,value):
        self.que=Node()
        self.que.data=value
    def isEmpty(self):
        return self.que==None
    def enqueue(self,value):
        temp=self.que
        while temp.next!= None:
            temp=temp.next
        temp2=Node()
        temp2.data=value
        temp.next=temp2
    def peek(self):
        if self.isEmpty():
            print("No value to peek")
        return self.que.data
    def dequeue(self):
        if self.isEmpty():
            print("Nothing to remove")
        temp=self.que
        temp=temp.next
        self.que=temp
