#get value of minimum partition required 
#such that each partition should be a palindrome
def isPalindrome(X, i, j):
 
    while i <= j:
        if X[i] != X[j]:
            return False
        i = i + 1
        j = j - 1
 
    return True

    
def Solve(s,i,j):
    if (i>=j):
        return 0
    if isPalindrome(s,i,j):
        return 0
    answer=float("inf")
    for k in range(i,j):
        temp=Solve(s,i,k)+Solve(s,k+1,j)+1
        answer=min(answer,temp)
    return answer
        

s ="ababbbabbababa"
n=len(s)
a=Solve(s,0,n-1)
print(a)
