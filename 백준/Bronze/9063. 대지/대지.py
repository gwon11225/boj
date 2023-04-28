n = int(input())
min_x,min_y,max_x,max_y = 10001,10001,-10001,-10001
for i in range(n):
    x,y = map(int,input().split())
    if min_x >= x:
        min_x = x
    if min_y >= y:
        min_y = y
    if max_x <= x:
        max_x = x
    if max_y <= y:
        max_y = y
print((max_x - min_x)*(max_y - min_y))