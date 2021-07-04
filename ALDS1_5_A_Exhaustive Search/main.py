n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))
for m in M:
  s = 0
  for i in range(2 ** n):
      x = 0
      for j in range(n):  # このループが一番のポイント
          if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
              x += A[j]  # フラグが立っていたら bag に果物を詰める
      if x == m:
        s =1
  if s == 1:
    print("yes")
  else:
    print("no")
