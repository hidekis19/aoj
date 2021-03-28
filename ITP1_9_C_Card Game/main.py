taro = 0
hanako = 0

n = int(input())
n_list = []
for i in range(n):
    n_list.append(list(input().split()))

for j in n_list:
    j_taro = j[0]
    j_hanako = j[1]

    if j_taro == j_hanako:
        taro += 1
        hanako += 1
    else:
        j_sorted = sorted(j,reverse=True)
        if j_sorted == j:
            taro += 3
        else:
            hanako += 3

print(taro,hanako)