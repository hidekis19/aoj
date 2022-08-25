def dps(x,y):
    dp = [[0 for i in range(len(y)+1)] for j in range(len(x)+1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i+1][j+1] = max(dp[i][j] + 1,
                                dp[i+1][j],
                                dp[i][j+1])
            else:
                if dp[i+1][j] >= dp[i][j+1]:
                    dp[i+1][j+1] = dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
    return dp

n = int(input())
X = []
Y = []
for i in range(n):
    X.append(input())
    Y.append(input())

ans = []

for i in range(n):
    s = X[i]
    t = Y[i]
    l = dps(s,t)
    ans.append(l[len(s)][len(t)])

for a in ans:
    print(a)


                




