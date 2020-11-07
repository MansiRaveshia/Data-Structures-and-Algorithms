def Solve(s,i,j,isTrue):
    if i>j:
        return False
    if i==j:
        if isTrue==True:
            return s[i]=="T"
        else:
            return s[i]=="F"
    a=0
    for k in range(i+1,j,2):
        lt=Solve(s,i,k-1,True)
        lf=Solve(s,i,k-1,False)
        rt=Solve(s,k+1,j,True)
        rf=Solve(s,k+1,j,False)
        if (s[k]=='&'):
            if isTrue==True:
                a=a+(lt*rt)
            else:
                a=a+(lf*rt)+(lf*rf)+(lt*rf)
        if (s[k]=='|'):
            if isTrue==True:
                a=a+(lt*rt)+(lt*rf)+(lf*rt)
            else:
                a=a+(lf*rf)
        if (s[k]=='^'):
            if isTrue==True:
                a=a+(lt*rf)+(lf*rt)
            else:
                a=a+(lf*rf)+(lt*rt)

    return a



s1="T|T&F^T"
print(Solve(s1,0,len(s1)-1,True))
            
