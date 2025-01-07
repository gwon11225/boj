import sys
import heapq

num = int(input())
arr = []

for _ in range(num):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr, -x)