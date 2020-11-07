from singlylinklist import LinkedList,Node

class Solution:
    def merge2lists(self,l1,l2):
        ptr=LinkedList()            
        ptr.head=Node(0)
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                ptr.next=l2
                ptr=ptr.next
                print(ptr.data)
                break
            elif l2 is None:
                ptr.next=l1
                ptr=ptr.next
                print(ptr.data)
                break
            else :
                while l1 is not None and l2 is not None:
                    smaller=0
                    if l1.data<l2.data:
                        smaller=l1.data
                        l1=l1.next
                    else :
                        smaller=l2.data
                        l2=l2.next
                    new=Node(smaller)
                    ptr.next=new
                    ptr=ptr.next
                    print(ptr.data)
                    
                while l1:
                    ptr.next=Node(l1.data)
                    ptr=ptr.next
                    print(ptr.data)
                    l1=l1.next
                    
                while l2:
                    ptr.next=Node(l2.data)
                    ptr=ptr.next
                    print(ptr.data)
                    l2=l2.next
                    
                break
        return 

l1=LinkedList()
l2=LinkedList()
l1.append(1)
l1.append(3)
l1.append(4)
l1.append(17)
l1.append(18)
l1.append(48)
l1.append(66)

l2.append(2)
l2.append(3)
l2.append(6)
l2.append(13)
l2.append(25)

l1.print_list()
l2.print_list()
print()
l=Solution()
l.merge2lists(l1.head,l2.head)

