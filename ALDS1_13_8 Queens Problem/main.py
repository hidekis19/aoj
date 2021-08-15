import itertools

n = int(input())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))

P = itertools.permutations(range(8),8)
P = list(P)

for p in P:
    X =[]
    y =0
    for i,pi in enumerate(p):
        X.append([i,pi])
    for a in A:
        if a in X:
            y += 1
    if n == y:
        s = 0
        for ii,j in enumerate(p):
            for k in range(1,8):
                if ii +k <=7 and  (j+k == p[k+ii]  or j-k == p[k+ii]):
                    s =1
                    
        if s ==0:
            for pp in p:
                s = ""
                for a in range(8):
                    if a == pp:
                        s = s + 'Q'
                    else:
                        s = s + '.'
                print(s)









