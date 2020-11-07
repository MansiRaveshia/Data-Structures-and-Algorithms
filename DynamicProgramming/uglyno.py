def find_nth_ugly_no(n):
    i5=i2=i3=0
    u=[0]*n
    u[0]=1
    multiple_of2=u[i2]*2
    multiple_of3=u[i3]*3
    multiple_of5=u[i5]*5
    for i in range(1,n): 
        u[i]=min(multiple_of2,multiple_of3,multiple_of5)
        if(u[i]==multiple_of2):
            i2+=1
            multiple_of2=u[i2]*2
        if(u[i]==multiple_of3):
            i3+=1
            multiple_of3=u[i3]*3
        if(u[i]==multiple_of5):
            i5+=1
            multiple_of5=u[i5]*5
    return u[n-1]

print(find_nth_ugly_no(150))



