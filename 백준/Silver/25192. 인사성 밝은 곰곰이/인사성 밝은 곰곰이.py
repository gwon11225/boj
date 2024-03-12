from sys import stdin

n = int(input())

s = set()

answer = 0

for _ in range(n):
    cmd = input()

    if cmd == "ENTER":
        answer += len(s)
        s = set()
    else:
        s.add(cmd)
        
answer += len(s)
print(answer)