def pri(n_start,n_end,n):
    n_start = int(n_start)
    n_end = int(n_end)
    x = n[n_start:n_end+1]
    print(x)

def rev(n_start,n_end,n):
    n_start = int(n_start)
    n_end = int(n_end)
    x_1 = ''
    x_3 = ''
    if n_start >0:
        x_1 = n[:n_start]
    x_2 = n[n_start:n_end+1]
    x_2 =''.join(list(reversed(x_2)))
    if n_end <= len(n):
        x_3 = n[n_end+1:]
    return x_1 + x_2 + x_3

def rep(n_start,n_end,n,rep):
    n_start = int(n_start)
    n_end = int(n_end)
    x_1 = ''
    x_3 = ''
    if n_start >0:
        x_1 = n[:n_start]
    if n_end <= len(n):
        x_3 = n[n_end+1:]
    return x_1 + rep + x_3


str = input()
q = input()
n_list = []
for i in range(int(q)):
    n_list.append(list(input().split()))



for j in n_list:
    p = j[0]
    s = int(j[1])
    e = int(j[2])
    if p =='print':
         pri(s,e,str)
    elif  p=='replace':
        str =rep(s,e,str,j[3])
    elif  p=='reverse':
        str = rev(s,e,str)
        


