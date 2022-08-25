n,w = map(int,input().split())
vList = []
uList = []

for i in range(n):
    v,u = map(int,input().split())
    vList.append(v)
    uList.append(u)


dp = [[0 for i in range(w+2)] for j in range(n+2)]
dp[0][w] = 0

for i in range(n):
    for j in range(w+1):
        if j >= uList[i]:
            dp[i+1][j] = max(dp[i][j- uList[i]] + vList[i],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[n][w])
print(dp)
