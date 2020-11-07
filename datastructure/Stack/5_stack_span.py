def ngl(a):
    l=[]
    stack=[]
    for j in range(len(a)):
        if len(stack)==0:
            l.append(1)
        elif (len(stack)>0 and stack[-1][0]>a[j]):
            l.append(j-stack[-1][-1])
        elif (len(stack)>0 and stack[-1][0]<a[j]):
            while(len(stack)>0 and stack[-1][0]<=a[j]):
                stack.pop()
            if len(stack)==0:
                l.append(j+1)
            else:
                l.append(j-stack[-1][-1])
        stack.append((a[j],j))
    return l


price = [10, 4, 5, 90, 120, 80] 
print(ngl(price))

