class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
class Stack:
    def __init__(self,value):
        self.stack=Node()
        self.stack.data=value
    def peek(self):
        if self.isEmpty():
            print("Nothing to peek stack is empyty")
        return self.stack.data
    def push(self,value):
        temp=Node()
        temp.data=value
        temp2=self.stack
        temp.next=temp2
        self.stack=temp
    def pop(self):
        if self.isEmpty():
            print("Nothing to pop from the stack")
        temp=self.stack
        temp=temp.next
        self.stack=temp
    def isEmpty(self):
        return self.stack==None
