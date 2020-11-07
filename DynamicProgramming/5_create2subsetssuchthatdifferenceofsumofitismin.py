def Subsets(set, n): 
    sum=0
    for j in range(n):
        sum+=set[j]
    S=([[False for x in range(sum+1)] for y in range(n+1)])
    for j in range(n+1):
        S[j][0]=True
    for j in range(1,sum+1):
        S[0][j]=False
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]>j:
                S[i][j]=S[i-1][j]
            if j>= set[i-1]: 
                S[i][j]=(S[i-1][j] or S[i-1][j-set[i-1]])

    # Initialize difference of two sums.  
    diff = sum; 
      
    #Find the largest j such that S[n][j] 
    # is true where j loops from sum/2 t0 0 
    for j in range(sum//2+1):
        if S[n][j] == True:
            diff=min( diff,sum-2*j)
    return diff


arr = [3, 1, 4, 2, 2, 1]
n=len(arr)
print(Subsets(arr, n))
arr = [5, 13, 11, 1]
n=len(arr) 
print(Subsets(arr, n))
