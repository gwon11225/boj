from sys import stdin
print(*sorted([int(stdin.readline().rstrip()) for _ in range(int(stdin.readline().rstrip()))]))