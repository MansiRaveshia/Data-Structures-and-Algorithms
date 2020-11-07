from singlylinklist import LinkedList,Node
def sumlist(l1,l2):
    x=l1.head
    y=l2.head
    carry=0
    s=LinkedList()
    while x or y:
        if not x:
            i=0
        else:
            i=x.data
        if not y:
            j=0
        else:
            j=y.data
        z=i+ j + carry
        if z>=10:
            carry=1
            r=z%10
            s.append(r)
        else:
            carry=0
            s.append(z)
        if x:
            x=x.next
        if y:
            y=y.next

    s.print_list()

l1=LinkedList()
l2=LinkedList()
l1.append(1)
l1.append(3)
l1.append(4)

l2.append(2)
l2.append(3)
l2.append(7)
#l2.append(13)

sumlist(l1,l2)
        