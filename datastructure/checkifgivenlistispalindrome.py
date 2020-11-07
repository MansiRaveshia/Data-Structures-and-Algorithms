from singlylinklist import LinkedList,Node
def palindrome(self):
    c=self.head
    s=""
    while c:
        s+=c.data
        c=c.next
    return s==s[::-1]

l=LinkedList()
l.append("A")
l.append("B")
l.append("C")
l.append("D")
print(palindrome(l))
l1=LinkedList()
l1.append("A")
l1.append("B")
l1.append("C")
l1.append("B")
l1.append("A")
print(palindrome(l1))