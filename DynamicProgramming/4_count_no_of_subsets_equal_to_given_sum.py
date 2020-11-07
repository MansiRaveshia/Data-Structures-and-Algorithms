def SubsetsCount(set, n, sum): 
    S=([[0 for x in range(sum+1)] for y in range(n+1)])
    for j in range(n+1):
        S[j][0]=1
    for j in range(1,sum+1):
        S[0][j]=0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if set[i-1]>j:
                S[i][j]=S[i-1][j]
            if j>= set[i-1]: 
                S[i][j]=(S[i-1][j] + S[i-1][j-set[i-1]])

    return S[n][sum]


set = [ 3, 3, 3, 3 ]
n = len(set)  
sum = 6
print(SubsetsCount(set,n,sum))  
arr = [1, 2, 3, 3]
X = 6
print(SubsetsCount(arr,len(arr),X))  
arr= [1, 1, 1, 1] 
X = 1
print(SubsetsCount(arr,len(arr),X)) 
