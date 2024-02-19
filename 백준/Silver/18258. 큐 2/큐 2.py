from collections import deque
from sys import stdin
n = int(stdin.readline().rstrip())

q = deque()

for _ in range(n):
    cmd = stdin.readline().rstrip()
    match cmd:
        case "pop":
            print(-1 if len(q) == 0 else q.pop())
        case "size":
            print(len(q))
        case "empty":
            print(1 if len(q) == 0 else 0)
        case "front":
            print(-1 if len(q) == 0 else q[-1])
        case "back":
            print(-1 if len(q) == 0 else q[0])
        case _:
            _, value = cmd.split()
            q.appendleft(value)