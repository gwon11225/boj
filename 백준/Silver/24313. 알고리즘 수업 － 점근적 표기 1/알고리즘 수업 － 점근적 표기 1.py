a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 <= c and a1 * n0 + a0 <= c * n0:
    print(1)
else:
    n = n0 + 1
    while n <= 100:
        if a1 * n + a0 > c * n:
            print(0)
            break
        n += 1
    else:
        print(1)