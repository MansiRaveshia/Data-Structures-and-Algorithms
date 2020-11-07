# Python implementation to 
# count number of ways to  
# tile a floor of size n x m 
# using 1 x m tiles 
  
def countWays(n, m): 
    count=[0]*(n+1)
    count[0]=0
    for i in range(1,n+1):
        if i>m:
            count[i]=count[i-1]+count[i-m]
        elif (i<m or i==1):
            count[i]=1
        else:
            count[i]=2   #when i==m
    return count[n] 
  
  
  
n = 7
m = 4
  
print("Number of ways = ", countWays(n, m)) 
  


