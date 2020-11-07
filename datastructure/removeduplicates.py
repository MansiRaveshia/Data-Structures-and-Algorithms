from singlylinklist import LinkedList,Node
def removeduplicate(self):
    cur=self.head
    prev=None
    dup_val=dict()
    while cur:
        if cur.data in dup_val:
            prev.next=cur.next
            cur=None
        else:
            dup_val[cur.data]=1
            prev=cur
        cur=prev.next
    

def count_occurences(self,data):
    cur=self.head
    count=0
    while cur:
        if cur.data==data:
            count+=1
        cur=cur.next
    print(str(data) + " occures for " +str(count)+" times")
    




l1=LinkedList()
l1.append(3)
l1.append(4)
l1.append(17)
l1.append(17)
l1.append(48)
l1.append(4)
l1.append(3)
l1.print_list()
print()
count_occurences(l1,17)
removeduplicate(l1)
l1.print_list()
