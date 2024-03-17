from sys import stdin
from collections import Counter

n, length = map(int, stdin.readline().rstrip().split())

arr = []

for _ in range(n):
    word = stdin.readline().rstrip()

    if len(word) >= length:
        arr.append(word)

arr.sort()
arr.sort(key= lambda x: -len(x))

count = Counter(arr).most_common()

for i in count:
    print(i[0])