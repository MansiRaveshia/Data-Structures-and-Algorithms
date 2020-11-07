def permutationCoeff(n, k): 
    p=[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if(j==0):
                p[i][j]=1
            else:
                p[i][j]=p[i-1][j]+(j*p[i-1][j-1])
    return p[n][k]


n = 10
k = 2
print("Value fo P(", n, ", ", k, ") is ", 
       permutationCoeff(n, k), sep = "") 

