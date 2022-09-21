import math
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

while True:
    n = int(input())
    if n ==0:
        exit()
    XYZR = [list(map(float,input().split())) for i in range(n)]
    ABC = []
    fee = []
    for i,xyzr1 in enumerate(XYZR):
        for j,xyzr2 in enumerate(XYZR):
            if i != j:
                s = math.sqrt((xyzr1[0]-xyzr2[0])**2+(xyzr1[1]-xyzr2[1])**2+(xyzr1[2]-xyzr2[2])**2)
                distance=max(s - xyzr1[3] -xyzr2[3],0)
                ABC.append([i,j,distance])
    ABC = sorted(ABC,key = lambda x:(x[2]))
    uni = UnionFind(n)
    for a,b,c in ABC:
        if uni.issame(a,b):
            continue
        fee.append(c)
        uni.unite(a,b)
    print(f"{sum(fee):.3f}")
    



