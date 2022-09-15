from re import S


# V: 頂点数
# g[v] = {(w, cost)}:
#     頂点vから遷移可能な頂点(w)とそのコスト(cost)
# r: 始点の頂点
 
from heapq import heappush, heappop
INF = 10**10
def dijkstra(N, G, s):
    dist = [INF] * N
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist

v,e,r = map(int,input().split())
std = [list(map(int,input().split())) for _ in range(v)]

V = [[]]*v
for s,t,d in std:
    V[s].append([t,d])
X = dijkstra(v,V,r)
ans = 0
for x in X:
    ans += x
    if x > 10**9:
        print("INF")
        continue
    print(ans)
