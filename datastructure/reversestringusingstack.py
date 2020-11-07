from stack import Stack

def rev(st):
    s=Stack()
    
    for i in range(len(st)):
        s.push(st[i])

    required=""
    while not s.is_empty():
        required+=s.pop()
    
    return required

print(rev(""))
print(rev("Mansi Shrey"))
print(rev("Mansi"))



