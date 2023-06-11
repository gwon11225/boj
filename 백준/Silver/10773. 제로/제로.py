from sys import stdin
n = int(stdin.readline().rstrip())
arr = []
for i in range(n):
    req = int(stdin.readline().rstrip())
    if req == 0:
        arr.pop()
        continue
    arr.append(req)
print(sum(arr))