while True:
    x = input()
    if x[0] == '0' : break
    y = list(x)
    l_si_i = [int(s) for s in y]
    print(sum(l_si_i))

