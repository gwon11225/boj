a,b = map(int,input().split())
c = a
d = b
while d:
    c,d = d,c%d
print(c)
print(a*b//c)