import sys 
inp = [] 
for i in sys.stdin.readlines(): 
    inp.append(i.rstrip()) 

for i  in inp:
    #区切り文字で判断して文字列からリストに変換
    i = i.split(' ',2)
    if (int(i[0]) == -1) and (int(i[1]) == -1 ) and (int(i[2]) == -1 ) :
        break
    if int(i[0]) == -1 or int(i[1]) == -1 :
        ans = 'F'
    else :
        if int(i[0]) == -1:
            i[0] = 0
        if int(i[1]) == -1:
            i[1] = 0
        if int(i[2]) == -1:
            i[2] = 0
        total = int(i[0]) + int(i[1]) 
        if total >= 80:
            ans = 'A'
        elif total >= 65:
            ans = 'B'
        elif total >= 50:
            ans = 'C'
        elif int(i[2]) >= 50:
            ans = 'C'
        elif total >= 30:
            ans = 'D'
        else :
            ans = 'F'
    print(ans)




