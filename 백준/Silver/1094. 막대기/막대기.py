n = int(input())
cnt = 0
a = 0
while n:
    for i in range(7):
        if n >= 2**i:
            a = i
    n -= 2**a
    cnt += 1
print(cnt)