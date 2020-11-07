#rotating singly linked list about kth position
from singlylinklist import LinkedList,Node
def rotate(self,k):
    if k==0:
        return
    c=self.head
    while c.next:
        c=c.next
    # c will now point to last node in list 
    a=self.head
    pos=1
    while a and pos<k:
        a=a.next
        pos+=1
    #a will be the pointer after which we want to rotate
    c.next=self.head
    self.head=a.next
    a.next=None

l1=LinkedList()
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(17)
l1.append(18)
l1.append(48)
l1.append(66)
rotate(l1,3)
l1.print_list()