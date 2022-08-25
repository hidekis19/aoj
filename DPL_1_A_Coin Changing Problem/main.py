INF = float('inf')
n,m = map(int,input().split())
C = [0] + list(map(int,input().split()))


dp = [[INF for i in range(n+1)] for j in range(m+1)]
dp[0][0] = 0

for i in range(1,m+1):
    for j in range(n+1):
        if j - C[i]>=0:
            dp[i][j] = min(dp[i-1][j- C[i]] + 1,
                            dp[i][j-C[i]] + 1,
                            dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])