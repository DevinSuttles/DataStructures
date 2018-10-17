class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node
#MUST START WITH VALUE For LinkedList
class LinkedList:
    def __init__(self,value):
        self.m_front=Node()
        self.m_size=1
        self.m_front.data=value
    def getSize(self):
        return self.m_size
    def search(self,value):
        temp=self.m_front
        while temp!=None:
            if temp.data==value:
                return True
            temp=temp.next
        return False
    def getEntry(self,position):
        if position<=1:
            return self.m_front.data
    def insert(self,position,value):
        if position==1:
            temp=Node()
            temp.data=value
            temp.next=self.m_front
            self.m_front=temp
        elif (self.m_size+1)==position:
            temp=self.m_front
            while temp.next!=None:
                temp=temp.next
            temp2=Node()
            temp2.data=value
            temp2.next=None
            temp.next=temp2
        else:
            temp=self.m_front
            temp2=Node()
            for i in range(1,position-1):
                temp=temp.next
            temp2.data=value
            temp2.next=temp.next
            temp.next=temp2
        self.m_size+=1
    def clear(self):
        self.m_size=0
        self.m_front = None
    def printList(self):
        temp=self.m_front
        while temp!=None:
            print(temp.data)
            temp=temp.next
    def remove(self,position):
        if self.m_size<=0:
            self.m_front=None
            self.m_size=0
        if position==1:
            temp=self.m_front
            temp=temp.next
            self.m_front=temp
        elif position==self.m_size:
            temp=self.m_front
            for i in range(1,position-1):
                temp=temp.next
            temp.next=None
        else:
            temp=self.m_front
            for i in range(1,position):
                temp=temp.next
            jumper=self.m_front
            while jumper.next != temp:
                jumper=jumper.next
            jumper.next=temp.next
        self.m_size-=1
