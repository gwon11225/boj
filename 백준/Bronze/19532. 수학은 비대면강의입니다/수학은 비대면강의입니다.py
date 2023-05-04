ax,by,c,dx,ey,f = map(int,input().split())
for x in range(-999,1000):
    for y in range(-999,1000):
        if x*ax+by*y == c and x*dx+y*ey == f:
            print(x,y)
            break