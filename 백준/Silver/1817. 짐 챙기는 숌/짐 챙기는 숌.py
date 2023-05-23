m,n = map(int,input().split())
if m == 0:
    print(0)
    exit()
arr = list(map(int,input().split()))
cnt = 0
sum = 0
for i in arr:
    if sum + i > n:
        cnt += 1
        sum = i
        continue
    sum += i
    if sum == n:
        cnt += 1
        sum = 0
if sum > 0:
    cnt += 1
print(cnt)