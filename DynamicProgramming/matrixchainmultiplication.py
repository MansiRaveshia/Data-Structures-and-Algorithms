#in this we will find min no of multiplications required 
# to multiply matrices with given dimensions in array
def mcm(arr,i,j):
    n=len(arr)
    t=[[-1 for col in range(n+1)]for row in range(n+1)]
    if t[i][j]==-1:
        if i>=j:
            return 0
        minimum=float("inf")
        for k in range(i,j):
            temp=mcm(arr,i,k)+mcm(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
            minimum=min(minimum,temp)
        t[i][j]=minimum
        return minimum
    else:
        return t[i][j]


arr = [1, 2, 3, 4, 3] 
n = len(arr)
print("Minimum number of multiplications is ", mcm(arr, 1, n-1)) 
arr = [1, 2, 3 ,4] 
size = len(arr) 
print("Minimum number of multiplications is " ,mcm(arr,1, size-1)) 

