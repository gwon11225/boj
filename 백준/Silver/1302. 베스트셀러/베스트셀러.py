n = int(input())
arr = []
dct = {}
ans = []
for i in range(n):
    arr.append(input())
for i in set(arr):
    dct[i] = 0
for i in arr:
    dct[i] += 1
maxx = max(dct.values())
for i in sorted(arr):
    if maxx == dct[i]:
        print(i)
        break