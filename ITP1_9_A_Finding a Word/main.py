W = input()

ans = 0
while True:
    t = input()
    if t == 'END_OF_TEXT':
        break
    t = t.lower()
    t_list = t.split()
    x = t_list.count(W)
    ans += x

print(ans)

