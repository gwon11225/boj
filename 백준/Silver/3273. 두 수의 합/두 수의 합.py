n = int(input())
ar = [0 for _ in range(2000000)]
arr = list(map(int, input().split()))
x = int(input())
cnt = 0

for i in arr:
    ar[i - 1] += 1

for i in arr:
    if ar[x - i - 1] > 0 and x - i - 1 <= 1000000:
        cnt += 1

print(cnt // 2)