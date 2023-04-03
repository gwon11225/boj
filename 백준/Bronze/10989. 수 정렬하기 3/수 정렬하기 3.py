import sys
arr = [0 for _ in range(10000)]
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    arr[a-1] += 1
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)