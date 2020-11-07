class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
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

    def prepend(self,data):
        new_node=Node(data)
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
                new_node.next=cur.next
                cur.next=new_node
                return
            else:  
                cur=cur.next
        
        if cur is None:
            print(prevdata+" i.e. item after which we want to insert is not found")
        
    def search(self,d):
        if self.head is None:
            print("list has no elements")
            return
        cur=self.head
        while cur is not None:
            if cur.data==d:
                print(d+" i.e. searched item is found")
                return ""
            cur=cur.next
        print(d+" i.e. searched item is not found")
        return ""

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
        n=None

    def deleteatpos(self,pos):
        if self.head is None:
            print("list has no elements")
            return
        n=self.head
        i=1
        if n and pos==1:
            self.head=n.next
            n=None
            return
        prev=None
        while n and i!=pos:
            prev=n
            n=n.next
            i+=1
        if n is None:
            print(" not found")
            return 
        prev.next=n.next
        n=None

    def length_recursive(self,Node):
        if Node is None:
            return 0
        return 1+self.length_recursive(Node.next)

    def swap(self,k1,k2):
        if self.head is None:
            print("list has no elements")
            return
        if (k1==k2):
            return
        k1prev=None
        k1c=self.head
        while k1c and k1c.data!=k1:
            k1prev=k1c
            k1c=k1c.next

        k2prev=None
        k2c=self.head
        while k2c and k2c.data!=k2:
            k2prev=k2c
            k2c=k2c.next
        #if k1 or k2 is not present
        if not k1c or not k2c:
            return
        #if x is not head
        if k1prev:
            k1prev.next=k2c
        else:
            self.head=k2c
        #if y is not head
        if k2prev:
            k2prev.next=k1c
        else:
            self.head=k1c
        k1c.next,k2c.next=k2c.next,k1c.next

    def reverse_list(self):
        prev=None
        current=self.head
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev 

            
l=LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.prepend("Z")
l.append("D")
l.print_list()
print()
l.swap("B","Z")
#l.insert_after_node("B","M")
#l.insert_after_node("V","K")
l.print_list()
#print(l.search("B"))
#print(l.search("S"))
#print(l.search("Z"))
print()
l.reverse_list()
l.print_list()
#l.delete("C")
#l.delete("G")
#l.print_list()
print()
#l.deleteatpos(2)
#l.delete("Z")
#l.print_list()
#print(l.length_recursive(l.head))




