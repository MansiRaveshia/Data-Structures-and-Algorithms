#given an array
#count no ways in which we can put sign infront of elements
#such that total of array after that equals given sum
def SubsetsCount(set, n, d): 
    sum_of_array=0
    for i in range(n):
        sum_of_array+=set[i]
    sum=(sum_of_array+d)//2

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
target_sum=0
print(SubsetsCount(set,n,target_sum))  
arr = [1,1, 2, 10,20]
target_sum=6
print(SubsetsCount(arr,len(arr),target_sum))  
arr= [1, 1, 1, 1] 
target_sum=2
print(SubsetsCount(arr,len(arr),target_sum))  
arr= [1, 2, 1,4] 
target_sum=2
print(SubsetsCount(arr,len(arr),target_sum))  
