import sys 
from itertools import combinations
inp = [] 
for i in sys.stdin.readlines(): 
    inp.append(i.rstrip()) 




for i in inp:
    i = i.split(' ',2)
    if int(i[0])==0 and int(i[1])==0:
        break
    N = int(i[1])
    ans_list = []
    for c1, c2 in combinations(range(1, int(i[0])), 2):
        a = c1
        b = c2 - c1
        c = N - c2
        ans_list.append([a,b,c])
    print(len(sorted(ans_list)))

 