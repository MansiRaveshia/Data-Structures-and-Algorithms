#check if string a is present in string b
#if yes then return true otherwise return false
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
    return L[m][n]==m or L[m][n]== n

X="AXY"
Y="ADXBCYE"
print(lcs(X,Y))
X="AXY"
Y="ADXBCE"
print(lcs(X,Y))
