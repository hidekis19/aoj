def binary_search(list, item):
    low = 0                        # lowとhighを使ってリストの検索部分を追跡
    high = len(list) - 1
    while low <= high:             # 1つの要素に絞り込まれるまでの間は...
        mid = (low + high) // 2
        guess = list[mid]          # 真ん中の要素を調べる
        if guess == item :          # アイテムを検出
            if mid-1 >=0 and list[mid-1] == item:
                high = mid - 1 
            else:
                return mid 
        elif guess > item:           # 推測した数字が大きすぎた
            high = mid - 1
        else:                      # 推測した数字が小さすぎた
            low = mid + 1
    return high +1                   # アイテムが存在しない

n = int(input())
A = [int(input()) for i in range(n)]

dp = [0 for i in range(n)]
L =  []
length = 0

for i in range(n):
    pos = binary_search(L,A[i])
    dp[i] = pos
    if dp[i] >= length:
        L.append(A[i])
        length += 1
    else:
        L[dp[i]] = A[i]
print(length)



