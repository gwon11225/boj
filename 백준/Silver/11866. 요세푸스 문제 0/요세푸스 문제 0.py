from collections import deque

cnt = 0

n, seq = map(int, input().split())

arr = [str(i) for i in range(1, n + 1)]

answer = []

for i in range(n):
    cnt += seq - 1
    cnt %= len(arr)
    answer.append(arr.pop(cnt))
    
print("<" + ", ".join(answer) + ">")