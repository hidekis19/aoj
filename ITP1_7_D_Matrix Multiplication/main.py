n,m,l= map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))
B=[]
for i in range(m):
    B.append(list(map(int,input().split())))

for a in A:
    C_line = []
    for j in range(l):
        b = [x[j] for x in B]
        c = [x*y for (x,y) in zip(a,b)]
        c = sum(c)
        C_line.append(c)   
    L=[str(a) for a in C_line]
    L=" ".join(L)     
    print(L)


