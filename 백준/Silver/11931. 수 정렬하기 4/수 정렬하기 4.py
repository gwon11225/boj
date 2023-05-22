from sys import stdin
for i in sorted([int(stdin.readline().rstrip()) for _ in range(int(input()))],reverse=True):
    print(i)