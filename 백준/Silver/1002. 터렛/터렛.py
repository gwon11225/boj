def sq(x):
    return x**2
n = int(input())
for i in range(n):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dist = (x1 - x2)**2 + (y1 - y2)**2
    if r1 == r2 and x1 == x2 and y1 == y2:
        print(-1)
    elif dist > sq(r1 + r2):
        print(0)
    elif dist == sq(r1 + r2):
        print(1)
    elif dist < sq(r1 + r2):
        if dist > sq(r2 - r1):
            print(2)
        elif dist == sq(r2 - r1):
            print(1)
        elif dist < sq(r2 - r1):
            print(0)