#count no of subsets that can be formed from given set such that difference of 
#sum of 2 subsets equals given difference
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
difference=0
print(SubsetsCount(set,n,difference))  
arr = [1,1, 2, 10,20]
difference1=6
print(SubsetsCount(arr,len(arr),difference1))  
arr= [1, 1, 1, 1] 
difference=2
print(SubsetsCount(arr,len(arr),difference))  
arr= [1, 2, 1,4] 
difference=2
print(SubsetsCount(arr,len(arr),difference))  
