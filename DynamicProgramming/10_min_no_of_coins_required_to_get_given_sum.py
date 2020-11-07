def count(a,n,sum):
    C=[[0 for j in range (sum+1)] for i in range(n+1)]
    for i in range(n+1):
        C[i][0]=0
    for j in range(sum+1):
        C[0][j]=float('inf') 
    for j in range(sum+1):
        if j%a[0]==0:
            C[1][j]=j//a[0]
        else:
            C[1][j]=float('inf')
    for i in range(2,n+1):
        for j in range(1,sum+1):
            if a[i-1]<=j:
                C[i][j]=min(1+C[i][j-a[i-1]],C[i-1][j])
            else:
                C[i][j]=C[i-1][j]
    return C[n][sum]


coins = [9, 6, 5, 1] 
n = len(coins) 
V = 11
print(count(coins,n,V))
coins = [25, 10, 5]
V = 30
n = len(coins) 
print(count(coins,n,V))