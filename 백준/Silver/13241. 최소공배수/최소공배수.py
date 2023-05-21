a,b = map(int,input().split())
c,d = a,b
while b:
    a,b = b,a%b
print((c*d)//a)