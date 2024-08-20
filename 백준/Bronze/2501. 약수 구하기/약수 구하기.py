count = 0

n, k = map(int, input().split())

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
    if count == k:
        print(i)
        exit()
print(0)