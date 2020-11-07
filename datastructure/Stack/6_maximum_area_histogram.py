def hist(a):
    #for index at right
    l=[]
    stack=[]
    for j in range(len(a)-1,-1,-1):
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
    l=l[::-1]

#for index at left
    m=[]
    st=[]
    for j in range(len(a)):
        if len(st)==0:
            m.append(-1)
        elif (len(st)>0 and st[-1]<a[j]):
            m.append(st[-1])
        elif (len(st)>0 and st[-1]>a[j]):
            while(len(st)>0 and st[-1]>=a[j]):
                st.pop()
            if len(st)==0:
                m.append(-1)
            else:
                m.append(st[-1])
        st.append(a[j])
#to make list of all areas 
    r=[]
    for j in range(len(a)):
        r.append((l[j]-m[j]-1)*a[j])


    return max(r)

    
h = [6, 2, 5, 4, 5, 1, 6] 
print(hist(h))
h=[1,2,3,4,5]
print(hist(h))