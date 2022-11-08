v,e = map(int,input().split())
inf = 10**9

dist = [[inf]*v for i in range(v)]

for i in range(e):
    s,t,d = map(int,input().split())
    dist[s][t] = d

dp = [[inf]*v for i in range(2**v)]
dp[0][0] = 0

for i in range(2**v):
    for j in range(v):
        if dp[i][j] < inf:
            for k in range(v):
                if (i // (2**k)) %2 == 0:
                    dis = dp[i][j] + dist[k][j]
                    if dp[i+(2**k)][k] > dis:
                        dp[i+(2**k)][k] = dis
ans = dp[2**v-1][0]

if ans == inf:
    print(-1)
else:
    print(ans)


