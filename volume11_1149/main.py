def func(li,weight,hight):
    P = [[hight,weight]]
    cakes = []
    for p,ins in li:
        cake_h,cake_w = P.pop(p-1)
        if not (cake_h == 0 and cake_w == 0):
            ins %= cake_h*2 + cake_w*2
        if ins <= cake_w:
            if ins <= cake_w//2:
                P.append([cake_h,ins])
                P.append([cake_h,cake_w-ins])
            else:
                P.append([cake_h,cake_w-ins])
                P.append([cake_h,ins])
        elif ins - cake_w <=  cake_h:
            ins -= cake_w
            if ins <= cake_h//2:
                P.append([ins,cake_w])
                P.append([cake_h-ins,cake_w])
            else:
                P.append([cake_h-ins,cake_w])
                P.append([ins,cake_w])
        elif ins - cake_w - cake_h <= cake_w:
            ins -= cake_w + cake_h
            if ins <= cake_w//2:
                P.append([cake_h,ins])
                P.append([cake_h,cake_w-ins])
            else:
                P.append([cake_h,cake_w-ins])
                P.append([cake_h,ins])
        else:
            ins -= cake_w*2 + cake_h
            if ins <= cake_h//2:
                P.append([ins,cake_w])
                P.append([cake_h-ins,cake_w])
            else:
                P.append([cake_h-ins,cake_w])
                P.append([ins,cake_w])
    for ph,pw in P:
        cakes.append(ph*pw)
    return sorted(cakes)
while True:
    n,w,d = map(int,input().split())
    if n == w == d ==0:
        exit()
    PS = [list(map(int,input().split())) for i in range(n)]
    x = func(PS,w,d)
    print(*x)

