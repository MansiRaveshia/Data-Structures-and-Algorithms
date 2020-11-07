# A Dynamic Programming solution for subset  
# sum problem Returns true if there is a subset of  
# set[] with sun equal to given sum  
  
# Returns true if there is a subset of set[]  
# with sun equal to given sum 
def isSubsetSum(set, n, sum): 
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

    return S[n][sum]


set = [3, 34, 4, 12, 5, 2] 
sum = 9
n = len(set) 
print(isSubsetSum(set, n, sum))

    
    