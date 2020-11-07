def lcs(X,Y):
    m=len(X)
    n=len(Y)
    L=[[0 for x in range(n+1)] for x in range(m+1)]
    result=0
    x=0
    y=0
    for i in range(m+1):
        for j in range(n+1):
            if (i==0 or j==0):
                L[i][j]=0
            elif X[i-1]==Y[j-1]:
                L[i][j]=1+L[i-1][j-1]
                if L[i][j]>result:
                    a=i
                    b=j
                result=max(result,L[i][j])
            else:
                L[i][j]=0
    S=""
    while result>0:
        S+=X[a-1]
        a=a-1
        result=result-1

    return S[::-1]


X = "GeeksforGeeks"
Y = "GeeksQuiz"
print(lcs(X,Y))
X = "zxabcdezy"
Y = "yzabcdezx"
print(lcs(X,Y))
X = "abcdxyz"
Y = "xyzabcd"
print(lcs(X,Y))
