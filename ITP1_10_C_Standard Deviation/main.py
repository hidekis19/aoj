
while True:
    n = int(input())
    if n == 0:
        break
    s = list(map(int, input().split())) 

    m = sum(s) / len(s)

    ss = 0
    for i in s:
        x = (i - m)**2
        ss += x
    
    α2 = ss/n
    α = α2**0.5
    print(α)


