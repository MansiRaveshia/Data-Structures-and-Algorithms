def ngr(a):
    l=[]
    stack=[]
    for j in range(len(a)-1,-1,-1):
        if len(stack)==0:
            l.append(-1)
        elif (len(stack)>0 and stack[-1]>a[j]):
            l.append(stack[-1])
        elif (len(stack)>0 and stack[-1]<a[j]):
            while(len(stack)>0 and stack[-1]<=a[j]):
                stack.pop()
            if len(stack)==0:
                l.append(-1)
            else:
                l.append(stack[-1])
        stack.append(a[j])
    return l[::-1]


arr = [11,13,21,3] 
print(ngr(arr))
a=[4, 5, 2, 25]
print(ngr(a))


