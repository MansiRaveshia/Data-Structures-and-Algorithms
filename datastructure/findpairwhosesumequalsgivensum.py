from doublylinklist import DoublyLinkedList,Node

def find(self,s):
    pairs=list()
    x=self.head
    y=None
    while x:
        y=x.next
        while y:
            if (x.data+y.data)==s:
                pairs.append("("+str(x.data)+","+str(y.data)+")")
            y=y.next
        x=x.next
    return pairs

l1=DoublyLinkedList()
l1.append(3)
l1.append(4)
l1.append(2)
l1.append(0)
l1.append(5)
l1.append(1)
l1.append(4)
print(find(l1,5))