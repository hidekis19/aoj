import sys 
from itertools import combinations
inp = [] 
for i in sys.stdin.readlines(): 
    inp.append(i.rstrip()) 

#1行ずつ見る
for i in inp:
    ans = 0
    i = i.split(' ',2)
    #終了条件
    if int(i[0])==0 and int(i[1])==0:
        break
    n = int(i[0])
    x = int(i[1])
    list_a = list(range(1,n-1))
    for a in list_a:
        list_b = list(range(a+1,n))
        for b in list_b:
            list_c = list(range(b+1,n+1))
            for c in list_c:
                if (a+b+c) == x:
                    ans += 1
    print(ans)




 