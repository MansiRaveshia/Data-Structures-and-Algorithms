class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            self.head.next=self.head
        else:
            c=self.head
            while c.next!=self.head:
                c=c.next
            c.next=new_node
            new_node.next=self.head

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        c=self.head
        if self.head is None:
            new_node.next=new_node
        else :
            while c.next!=self.head:
                c=c.next
            c.next=new_node
        self.head=new_node

    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
            if cur_node==self.head:
                break

    def remove(self,k):
        if self.head.data==k:
            c=self.head
            while c.next!=self.head:
                c=c.next
            c.next=self.head
            self.head=c.next
        else:
            c=self.head
            p=None
            while c.next!=self.head:
                p=c
                c=c.next
                if c.data==k:
                    p.next=c.next
                    c=None
                    break

    def length(self):
        c=self.head
        l=1
        while c.next!=self.head:
            c=c.next
            l+=1
        return l

    def splitlist(self,l):
        c=self.head
        l1=CircularLinkedList()
        l2=CircularLinkedList()
        x=0
        while x!=l//2:
            l1.append(c.data)
            c=c.next
            x+=1
        while x<=l and c!=self.head:
            l2.append(c.data)
            c=c.next
            x+=1

        l1.print_list()
        print()
        l2.print_list()

    def is_circular(self,l):
        c=self.head
        while c.next:
            c=c.next
            if c.next==self.head:
                return True
        return False

C=CircularLinkedList()
C.append("A")
C.append("B")
C.append("C")
C.prepend("Z")
C.append("D")
C.append("E")
C.append("F")
C.append("G")

C.print_list()
print()
l=C.length()
C.splitlist(l)
print()

C.remove("A")
C.remove("F")

C.print_list()
print(C.is_circular(C))








