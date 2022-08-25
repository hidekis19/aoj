import sys, os, math, bisect, itertools, collections, heapq, queue, copy, array

# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
# from decimal import Decimal
# from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def lcs(X, Y):
    dp = []
    for y in Y:
        bgn_idx = 0
        for i, cur_idx in enumerate(dp):
            # 既に探索済みの最長文字列を更新
            chr_idx = X.find(y, bgn_idx) + 1
            if not chr_idx:
                break
            dp[i] = min(chr_idx, cur_idx)
            bgn_idx = cur_idx
        else:
            chr_idx = X.find(y, bgn_idx) + 1
            if chr_idx:
                dp.append(chr_idx)
    return len(dp)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    for _ in range(N):
        X, Y = iss(), iss()
        print(lcs(X, Y))


if __name__ == '__main__':
    main()