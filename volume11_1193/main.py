def func(h,li):
    ans = 0
    S = []
    for i in zip(*li):
        S.append(list(reversed(i)))
    de = []
    while True:
        for j in range(h):
            cnt = 0
            ins = 0
            ind = j
            for i in range(5):
                if j < len(S[i]) :
                    if ins == S[i][j]:
                        cnt += 1
                        if i ==4 and cnt >=3:
                            de.append([ind,i-cnt+1,cnt])
                    elif cnt >=3:      
                        de.append([ind,i-cnt,cnt])
                        cnt = 1
                        ins = S[i][j]     
                        ind = j            
                    else:
                        cnt = 1
                        ins = S[i][j]     
                        ind = j
                else:
                    cnt = 0
                    ins = 0
        if not de:
            break
        while de :
            hi , wi , cn = de.pop()
            for i in range(wi,wi+cn):
                x = S[i].pop(hi)
                ans +=x
    return ans

while True:
    h = int(input())
    if h ==0:
        exit()
    rock = [list(map(int,input().split())) for i in range(h)]
    s = func(h,rock)
    print(s)


