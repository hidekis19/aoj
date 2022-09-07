n,w = map(int,input().split())
VW =[0] + [list(map(int,input().split())) for i in range(n)]

dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(w+1):
        if j-VW[i][1] >=0:
            dp[i][j] = max(dp[i][j],dp[i-1][j-VW[i][1]] + VW[i][0])
        dp[i][j] = max(dp[i][j],dp[i-1][j])

ans = 0
for d in dp[n]:
    ans = max(ans,d)
print(ans)
