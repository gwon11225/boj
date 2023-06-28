from functools import cmp_to_key
input()
arr = sorted(list(input().split()),key=cmp_to_key(lambda x, y: 1 if int(x+y) < int(y+x) else -1))
print(int("".join(arr)))