n = int(input())
arr = list(map(int, input().split()))
s = sorted(arr)
count = 0
answer = [0 for _ in range(n)]
for i in s:
    for j in range(n):
        if arr[j] == i and arr[j] != 'zz':
            answer[j] = count
            count += 1
            arr[j] = 'zz'
            break
print(*answer)