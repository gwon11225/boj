from itertools import *

n, m = map(int, input().split())

arr = list(map(int, input().split()))

answer = sorted(list(permutations(arr, 3)))

real_answer = 0

for i in answer:
    if sum(i) <= m:
        if real_answer < sum(i):
            real_answer = sum(i)

print(real_answer)