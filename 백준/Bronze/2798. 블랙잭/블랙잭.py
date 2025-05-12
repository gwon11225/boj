n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            t = arr[i] + arr[j] + arr[k]
            if t <= m and t >= s:
                s = t
print(s)