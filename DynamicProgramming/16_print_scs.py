#print shortest common supersequence
def scs(X,Y):
    m=len(X)
    n=len(Y)
    L=[[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=1+L[i-1][j-1]
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1]) 
    
    i=m
    j=n
    S=""
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            S+=X[i-1]
            i=i-1
            j=j-1
        elif L[i-1][j]>L[i][j-1]:
            S+=X[i-1]
            i=i-1
        else:
            S+=Y[j-1]
            j=j-1
    while i>0:
        S+=X[i-1]
        i=i-1
    while j>0:
        S+=Y[j-1]
        j=j-1

    return S[::-1]


x = "AGGTAB"
y = "GXTXAYB"
print(scs(x, y)) 
X = "HELLO"
Y = "GEEK"
print(scs(X, Y)) 
  