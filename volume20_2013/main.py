while True:
    n = int(input())
    if n == 0:
        exit()
    times = [0 for i in range(3*(10**5))]
    trains = []
    for i in range(n):
        a,b = map(str,input().split())
        a = int(a.replace(":",""))
        b = int(b.replace(":",""))
        trains.append([a,b])

    for a,b in trains:
        times[a] += 1
        times[b] -= 1

    for i in range(3*(10**5)-1):
        times[i+1] += times[i]

    print(max(times))
