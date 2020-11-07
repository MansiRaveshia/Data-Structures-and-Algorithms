from stack import Stack

def convert(dec):
    s=Stack()
    while dec>0:
        remainder=dec%2
        s.push(remainder)
        dec=dec//2
    bin_no=""
    while not s.is_empty():
        bin_no+=str(s.pop())
    return bin_no

print(convert(13))
print(convert(1))
print(convert(2))
print(convert(3))
print(convert(25))