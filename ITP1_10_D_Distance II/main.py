n = input()
x = list(map(int, input().split())) 
y = list(map(int, input().split())) 

p1 = 0
p2 = 0
p3 = 0
pn = 0

bb = 0
cc = 0

#p =1
for i, xn in enumerate(x):
    a = abs(xn - y[i])
    p1 += a

#p =2
for i, xn in enumerate(x):
    b = (xn -y[i])**2
    bb += b

p2 = bb**0.5

#p =3
for i, xn in enumerate(x):
    c = (abs(xn -y[i]))**3
    cc += c
p3 = cc**(1/3)

#p =無限大

for i, xn in enumerate(x):
    a = abs(xn - y[i])
    if pn < a:
        pn = a

print(p1)
print(p2)
print(p3)
print(pn)


