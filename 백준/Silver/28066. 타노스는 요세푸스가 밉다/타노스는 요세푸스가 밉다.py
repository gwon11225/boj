from collections import deque

a, b = map(int, input().split())
arr = deque([i for i in range(1, a + 1)])
while len(arr) != 1:
    first = arr.popleft()
    for i in range(b - 1):
        if len(arr) != 0: arr.popleft()
    arr.append(first)
print(arr[0])