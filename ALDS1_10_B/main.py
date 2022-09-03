n = int(input())
rcList = [list(map(int,input().split())) for _ in range(n)]
l = [rcList[0][0]]
for i,rc in enumerate(rcList):
        l.append(rc[1])

def matrixChainMultiplication(dims): 
    n = len(dims)
    # c[i、j] =スカラー乗法の最小数(つまり、コスト)
    # 行列`M[i] M[i+1]…M[j]=M[i…j]`を計算するために必要な
    #1つの行列を乗算するときのコストはゼロです
    c = [[0 for x in range(n + 1)] for y in range((n + 1))]
    for length in range(2, n + 1):        #サブシーケンスの長さ
        for i in range(1, n - length + 2):
            j = i + length - 1
            c[i][j] = 10**18
            k = i
            while j < n and k <= j - 1:
                c[i][j] = min(c[i][j],
                                c[i][k] + c[k + 1][j] + dims[i - 1] * dims[k] * dims[j])
                k = k + 1
    print(c)
    return c[1][n - 1]
print(matrixChainMultiplication(l))