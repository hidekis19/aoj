from heapq import heappush, heappop
INF = float("inf")
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n # 始点からの距離の初期化
    hq = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while hq:
        v = heappop(hq)[1] # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist

# ノード数, エッジ数, 始点ノード
v, e, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
adj = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    adj[s].append((t, d))
D = dijkstra(r, v)

for d in D:
    if d == INF:
        print("INF")
    else:
        print(d)


