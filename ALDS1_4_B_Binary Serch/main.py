def binary_search(list, item):
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:             # 1つの要素に絞り込まれるまでの間は...
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item:          # アイテムを検出
            return mid
        if guess > item:           # 推測した数字が大きすぎた
            high = mid - 1
        else:                      # 推測した数字が小さすぎた
            low = mid + 1
    return -1                    # アイテムが存在しない

n = int(input())
S = list(map(int,input().split()))
q = int(input())
T = list(map(int,input().split()))

x = []
for t in T:
    y = binary_search(S,t)
    if y != -1:
        x.append(y)

print(len(x))