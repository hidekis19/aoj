house =[[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]],[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]]

#枚数をnにセット
#各データをリストにセット
n = int(input())
#各データをリストにセット
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))

for i in num_list:
    b = i[0]-1
    f = i[1]-1
    r = i[2]-1
    v = i[3]
    house[b][f][r] = house[b][f][r] + v

x = 0
for i in house:
    for j in i:
        ans =" "
        for k in j:
            ans += str(k)
            ans += " "
        print(ans)
    if x== n:
        break
    print("####################")
    x += 1
