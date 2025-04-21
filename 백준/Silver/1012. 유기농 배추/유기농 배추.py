import sys
sys.setrecursionlimit(10000)

history = []

def onejo_not_zege(arr, x, y, m, n):
    history.append([x, y])
    zege(arr, x - 1, y, m, n)
    zege(arr, x, y - 1, m, n)
    zege(arr, x + 1, y, m, n)
    zege(arr, x, y + 1, m, n)

def zege(arr, x, y, m, n):
    if x < 0 or x >= m:
        return
    if y < 0 or y >= n:
        return
    if arr[y][x] == 0:
        return
    if history in [x, y]:
        return
    arr[y][x] = 0

    zege(arr, x - 1, y, m, n)
    zege(arr, x, y - 1, m, n)
    zege(arr, x + 1, y, m, n)
    zege(arr, x, y + 1, m, n)

t = int(input())
for i in range(t):
    history = []
    m, n, k = map(int, input().split())
    arr = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1: onejo_not_zege(arr, x, y, m, n)
    print(len(history))