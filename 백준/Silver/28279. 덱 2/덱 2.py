from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())

arr = deque()

for i in range(n):
    cmd = stdin.readline().rstrip().split()
    match cmd[0]:
        case '1':
            arr.appendleft(cmd[1])
        case '2':
            arr.append(cmd[1])
        case '3':
            print(-1 if len(arr) == 0 else arr.popleft())
        case '4':
            print(-1 if len(arr) == 0 else arr.pop())
        case '5':
            print(len(arr))
        case '6':
            print(1 if len(arr) == 0 else 0)
        case '7':
            print(-1 if len(arr) == 0 else arr[0])
        case '8':
            print(-1 if len(arr) == 0 else arr[-1])