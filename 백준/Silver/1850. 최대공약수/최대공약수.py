a,b = map(int,input().split())
while b:
    a,b = b,a%b
print("1"*a)