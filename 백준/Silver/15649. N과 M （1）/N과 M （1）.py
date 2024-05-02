from itertools import *

a, b = map( int, input().split() )
arr = [i for i in range(1, a + 1)]

answer = list(permutations(arr, b))

for i in answer:
    print(" ".join(list(map(str, i))))