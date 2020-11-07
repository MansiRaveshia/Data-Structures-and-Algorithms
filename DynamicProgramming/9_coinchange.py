#find the maximum nos of ways in which we can take the set of coins 
#to get the required max amount
def Coin(set, n, sum): 
    S=([[0 for x in range(sum+1)] for y in range(n+1)])
    for j in range(n+1):
        S[j][0]=1
    for j in range(1,sum+1):
        S[0][j]=0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]>j:
                S[i][j]=S[i-1][j]
            if set[i-1]<=j: 
                S[i][j]=(S[i-1][j] + S[i][j-set[i-1]])

    return S[n][sum]


arr = [1, 2, 3] 
m = len(arr) 
n = 4
print(Coin(arr, m, n)) 