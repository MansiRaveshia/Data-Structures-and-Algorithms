class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        l_node=self.head
        while l_node.next:
            l_node=l_node.next
        l_node.next=new_node
        new_node.prev=l_node

    def prepend(self,data):
        new_node=Node(data)
        self.head.prev=new_node
        new_node.next=self.head
        self.head=new_node

    def insert_after_givendata(self,prevdata,data):
        if self.head is None:
            print("list has no elements")
            return
        new_node=Node(data)
        cur=self.head
        while cur is not None:
            if cur.data==prevdata:
                new_node.prev=cur
                new_node.next=cur.next
                cur.next.prev=new_node
                cur.next=new_node
                return
            else:  
                cur=cur.next
        
        if cur is None:
            print(prevdata+" i.e. item after which we want to insert is not found")

    def insert_before_givendata(self,afterdata,data):
        if self.head is None:
            print("list has no elements")
            return
        new_node=Node(data)
        cur=self.head
        while cur:
            if cur.data==afterdata:
                new_node.next=cur
                new_node.prev=cur.prev
                cur.prev.next=new_node
                cur.prev=new_node
                if cur==self.head:
                    self.head=new_node
                return
            else:
                cur=cur.next

    def delete(self,key):
        if self.head is None:
            print("list has no elements")
            return
        n=self.head
        if  n and n.data==key:
            self.head=n.next
            n=None
            return
        prev=None
        while n and n.data!=key:
            prev=n
            n=n.next
        if n is None:
            print(key+" is not found")
            return 
        prev.next=n.next
        n.next.prev=prev
        n=None

    def reverse_list(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            current.prev=next
            prev=current
            current=next
        self.head=prev 


    def length_recursive(self,Node):
        if Node is None:
            return 0
        return 1+self.length_recursive(Node.next)
    



l=DoublyLinkedList()
l.append("A")
l.append("B")
l.append("C")
l.prepend("Z")
l.append("D")
l.print_list()
l.insert_after_givendata("B","M")
l.insert_after_givendata("V","K")
l.delete("C")
l.delete("G")
l.delete("Z")
l.print_list()
print()
l.insert_before_givendata("A","X")
l.insert_before_givendata("D","Y")
l.print_list()
print()
l.reverse_list()
l.print_list()
