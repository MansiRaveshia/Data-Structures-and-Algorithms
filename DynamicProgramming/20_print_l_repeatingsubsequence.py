#print longest repeating subsequence
def lrs(X,Y):
    m=len(X)
    n=len(Y)
    L=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                L[i][j]=0
            elif ((X[i-1]==Y[j-1]) and (i!=j)):
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1]) 

    i=m
    j=n
    S=""
    while i>0 and j>0:
        if L[i][j]==L[i-1][j-1]+1:
            S+=X[i-1]
            i=i-1
            j=j-1
        elif L[i][j]==L[i-1][j]:
            i=i-1
        else:
            j=j-1
    return S[::-1]


s = 'AABEBCDD'
print(lrs(s,s)) 
s = "aabb"
print(lrs(s,s)) 
