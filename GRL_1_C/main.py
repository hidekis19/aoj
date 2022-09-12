v,e = map(int,input().split())
std = [list(map(int,input().split())) for _ in range(e)]
INF = float('inf')
dp = [[INF]*(v) for __ in range(v)]

for s,t,d in std:
    dp[s][t] = d
for i in range(v):
    dp[i][i] = 0

for k in range(v):
    for i in range(v):
        for j in range(v):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k][j])

for i in range(v):
    if dp[i][i] <0:
        print("NEGATIVE CYCLE")
        exit()

for i in range(v):
    d = [str(i).replace("inf",'INF') for i in dp[i]]
    print(*d)