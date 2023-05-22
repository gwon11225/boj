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

while True:
    n = int(stdin.readline().rstrip())
    if n == 0:
        break
    arr = sieve(n*2)
    cnt = 0
    for i in range(n*2 + 1):
        if i > n and arr[i] == True:
            cnt += 1
    print(cnt)