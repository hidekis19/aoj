r,n= map(int, input().split())
num_list = []
for i in range(r):
    num_list.append(list(map(int,input().split())))

mat = []

for i in num_list:
    x =  sum(i)
    i.append(x)
    mat.append(i)

vec = []
for i in range(n+1):
    y = [x[i] for x in mat]
    vec.append(sum(y))

mat.append(vec)

for j in mat:
    L=[str(a) for a in j]
    L=" ".join(L)

    print(L)