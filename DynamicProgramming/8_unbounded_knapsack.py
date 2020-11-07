def unboundedKnapsack(W, n, val, wt): 
    K=[[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if w==0 or i==0:
                K[i][w]=0
            elif wt[i-1]<=w:
                K[i][w]= max(val[i-1]+K[i][w-wt[i-1]],K[i-1][w])
            else:
                K[i][w]=K[i-1][w]

    return K[n][W]

W = 100
val = [10, 30, 20] 
wt = [5, 10, 15] 
n = len(val) 
  
print(unboundedKnapsack(W, n, val, wt)) 
