n = int(input())
A = list(map(int,input().split()))
q = int(input())
M = list(map(int,input().split()))
A = sorted(A,reverse=True)
for m in M:
    s = 0
    if sum(A) < m:
        print('no')
    else:
        for i in range(2 ** n):
            x = 0
            for j in range(n):  # このループが一番のポイント
                if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
                    x += A[j]  # フラグが立っていたら bag に果物を詰める
                if x > m:
                    break
                elif x+sum(A[j:]) <m:
                    break
            if x == m:
                s =1
                print("yes")
                break
        if s==0:
            print('no')