from math import gcd
from sys import stdin
n = int(stdin.readline().rstrip())
arr = [int(stdin.readline().rstrip()) for _ in range(int(n))]
arr_1 = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
g = arr_1[0]
for i in range(len(arr_1)):
    g = gcd(g,arr_1[i])
answer = int((arr[n-1] - arr[0])/g) + 1 - n
print(answer)