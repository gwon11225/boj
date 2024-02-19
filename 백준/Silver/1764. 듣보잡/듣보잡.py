import sys
n, m = map(int, input().split())

s = set()
answer = []

for i in range(n):
    s.add(sys.stdin.readline().rstrip())
cnt = 0
for i in range(m):
    name = sys.stdin.readline().rstrip()
    if name in s:
        cnt += 1
        answer.append(name)

print(cnt)
for i in sorted(answer): print(i)