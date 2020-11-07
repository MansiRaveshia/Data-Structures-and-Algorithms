#count no of insertion and deletion required to convert
#from 1 given string to other given string 
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
    return (m+n-(2*L[m][n]))



str1 = "heap"
str2 = "pea" 
print(lcs(str1,str2))

str1 = "geeksforgeeks"
str2 = "geeks"
print(lcs(str1,str2))