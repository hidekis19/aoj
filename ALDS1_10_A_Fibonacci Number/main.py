n = int(input())

f = [0]*50

f[0] = 1
f[1] = 1

for k in range(2,50):
    f[k] = f[k-2] + f[k-1]

print(f[n])
