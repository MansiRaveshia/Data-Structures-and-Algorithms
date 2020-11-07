def nsl(a):
    l=[]
    stack=[]
    for j in range(len(a)):
        if len(stack)==0:
            l.append(-1)
        elif (len(stack)>0 and stack[-1]<a[j]):
            l.append(stack[-1])
        elif (len(stack)>0 and stack[-1]>a[j]):
            while(len(stack)>0 and stack[-1]>=a[j]):
                stack.pop()
            if len(stack)==0:
                l.append(-1)
            else:
                l.append(stack[-1])
        stack.append(a[j])
    return l


arr =[3,21,9,13,11]
print(nsl(arr))
a=[25,0,3,2,6,4]
print(nsl(a))
