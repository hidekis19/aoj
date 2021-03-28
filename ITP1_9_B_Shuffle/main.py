

while True:
    t = input()
    if t == '-':
        break
    n = int(input())
    h = [input() for i in range(n)]

    for i in h:
        i = int(i)
        card_f = t[0:i]
        card_b = t[i:]
        t = card_b + card_f
        t = card_b + card_f
    
    print(t)
