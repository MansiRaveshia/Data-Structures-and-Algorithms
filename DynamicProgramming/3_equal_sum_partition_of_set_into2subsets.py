# Returns true if arr[] can be  
# partitioned in two subsets of  
# equal sum, otherwise false 
def findPartition(arr, n): 
    sum=0
    for j in range(n):
        sum+=arr[j]
    if sum%2!=0:
        return False
    
    part=[[False for x in range(sum//2+1)] for x in range(n+1)]
    for j in range(sum//2+1):
        part[0][j]=False
    for j in range(n+1):
        part[j][0]=True
    for i in range(1,n+1):
        for j in range(1,sum//2+1):
            if arr[i-1]>j:
                part[i][j]=part[i-1][j]
            else:
                part[i][j]= (part[i-1][j] or part[i-1][j-arr[i-1]])
    return part[n][sum//2]


arr = [3, 1, 1, 2, 2, 1] 
n = len(arr) 
print(findPartition(arr, n))


