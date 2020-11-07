#find longest palindrome from given string
def lps(X,Y):
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


s = "GEEKSFORGEEKS"
print(lps(s,s[::-1]))
s= "GEEKS FOR GEEKS"
print(lps(s,s[::-1]))