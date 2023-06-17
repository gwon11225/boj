from math import lcm
n = int(input())
arr = list(map(int, input().split()))
lc = arr[0]
for i in range(1,n):
    lc = lcm(lc,arr[i])
if lc == max(arr):
    lc *= min(arr)
print(lc)