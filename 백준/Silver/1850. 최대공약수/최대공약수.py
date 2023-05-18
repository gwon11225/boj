a,b = map(int,input().split())
while b:
    a,b = b,a%b
for i in range(a):
    print(1,end="")