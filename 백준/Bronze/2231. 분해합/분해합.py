n = int(input())
for i in range(n // 2, n):
    arr = list(map(int, list(str(i))))
    if i + sum(arr) == n:
        print(i)
        exit()
print(0)