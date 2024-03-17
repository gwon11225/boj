from sys import stdin
from collections import Counter

n = int(stdin.readline().rstrip())

arr = sorted([int(stdin.readline().rstrip()) for _ in range(n)])

print(int(round(sum(arr) / n, 0)))

print(arr[len(arr) // 2])

if n == 1:
    print(arr[0])
else:
    count = Counter(arr).most_common(2)

    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])

print(abs(arr[0] - arr[-1]))