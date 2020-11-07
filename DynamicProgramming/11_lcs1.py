#longest common subsequence
def lcs(X,Y):
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
    return L[m][n]


X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X, Y)) 
X="ABCDGH"
Y=  "AEDFHR"
print ("Length of LCS is ", lcs(X, Y)) 