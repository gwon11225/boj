a = 3
n = int(input())
cnt = 0
while n > 0:
    n -= a
    cnt += 1
    a += 2
print(cnt)