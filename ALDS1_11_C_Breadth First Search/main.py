from sys import stdin
input = stdin.readline

from collections import deque, defaultdict
from copy import deepcopy

INFTY = -1   # 探索しなかったやつを-1としてprintしやすくするために-1とした。

n = int(input())

M = [[0]*n for _ in range(n)]

def bfs(s):
    q = deque()
    q.append(s)
    d = [INFTY]*n
    d[s] = 0
    while q: # qが空だとwhileループから抜ける
        u = q.popleft()  # pythonのdequeはpopleft関数で戻り値がpopした要素になる
        for v in range(n):
            if M[u][v] == 0:
                continue
            if d[v] != INFTY:
                continue
            d[v] = d[u] + 1
            q.append(v)
    for i in range(n):
        print(str(i+1) + ' ' + str(d[i]))

for _ in range(n):
    u, k, *vv = map(int, input().split())
    u -= 1
    for v in vv:
        v -= 1
        M[u][v] = 1
bfs(0)