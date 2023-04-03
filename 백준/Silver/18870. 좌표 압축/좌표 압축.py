import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = sorted(set(a))
c = {b[i]: i for i in range(len(b))}
for i in a:
    print(c[i], end=' ')