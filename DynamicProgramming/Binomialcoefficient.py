def Binomial(n,k):
    c=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(k,i)+1):
            if j==0 or j==i:
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    return c[n][k]


n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
      + str(Binomial(n,k))) 
