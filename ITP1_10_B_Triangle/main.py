import math

a, b, C= map(int, input().split())

sinC = math.sin(math.radians(C))

S = a * b* sinC /2
h = b* sinC

x = (b**2 -h**2)**0.5

if C <= 90:
    c = (h**2 + (a-x)**2 )**0.5
else:
    c = ((a+x)**2 + h**2)**0.5

print(S)
print(a+b+c)
print(h)
