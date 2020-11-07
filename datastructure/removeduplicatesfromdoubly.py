from doublylinklist import DoublyLinkedList,Node

def removeduplicate(self):
    cur=self.head
    prev=None
    dup_val=dict()
    while cur:
        if cur.data in dup_val:
            prev.next=cur.next
            if cur.next:
                cur.next.prev=prev
            cur=None
        else:
            dup_val[cur.data]=1
            prev=cur
        cur=prev.next


l1=DoublyLinkedList()
l1.append(3)
l1.append(4)
l1.append(17)
l1.append(17)
l1.append(48)
l1.append(4)
l1.append(3)
l1.print_list()
print()
removeduplicate(l1)
l1.print_list()

    