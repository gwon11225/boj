import sys
input = sys.stdin.readline

sqrList = [[0], [1], [2, 4, 8, 6], [3, 9, 7, 1], [4, 6],
           [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1], [10]]

for _ in range(int(input())):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        a = 10
    ans = sqrList[a][b % len(sqrList[a]) - 1]
    print(ans)