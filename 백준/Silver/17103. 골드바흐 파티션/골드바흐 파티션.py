import math # sqrt
from sys import stdin

def sieve(n):
    arr = [True] * (n+1)
    arr[0] = False; arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i]:
            j = 2
            while i*j <= n: 
                arr[i*j] = False
                j += 1
    return arr

n = int(input())
for i in range(n):
    a = int(stdin.readline().rstrip())
    cnt = 0
    check = sieve(a)
    for i in range(1,a//2 + 1):
        if check[i] == True and check[a - i] == True:
            cnt += 1
    print(cnt)