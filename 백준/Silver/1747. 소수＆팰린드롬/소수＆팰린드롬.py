import math # sqrt

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
arr = sieve(1100000)
for i in range(1100000):
    if arr[i] == True and i >= n:
        if str(i) == str(i)[::-1]:
            print(i)
            break