from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))
answer = []
arr = deque()

for i in range(n):
    if a[i] == 0: arr.append(b[i])

for i in range(m):
    arr.appendleft(c[i])
    answer.append(arr.pop())
    
print(*answer)