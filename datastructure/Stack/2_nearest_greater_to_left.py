def ngl(a):
    l=[]
    stack=[]
    for j in range(len(a)):
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
    return l


arr =[3,21,13,11]
print(ngl(arr))
a=[25,2,5,4]
print(ngl(a))


