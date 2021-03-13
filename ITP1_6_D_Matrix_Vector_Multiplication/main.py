n,m= map(int, input().split())

mat = [input() for i in range(n)]

vec = [input() for i in range(m)]

vec_2 = [int(s) for s in vec]


for i in mat:
    i = i.split(' ')
    i_2 = [int(s) for s in i]
    s = [x*y for (x,y) in zip(i_2,vec_2)]
    print(sum(s))

        

