def bell_no(n):
    b=[[0 for j in range(n+1)] for i in range(n+1)]
    b[0][0]=1
    for i in range(1,n+1):
        b[i][0]=b[i-1][i-1]
        for j in range(1,i+1):
            b[i][j]=b[i-1][j-1]+b[i][j-1]
    return b[n][0]


for j in range(6):
    print('Bell Number', j, 'is', bell_no(j)) 