n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key= lambda x:(x[1]))
start_time = arr[0][1] - arr[0][0]
while start_time > 0:
    cnt = 0
    sum_time = start_time
    for i in range(n):
        sum_time += arr[i][0]
        if sum_time > arr[i][1]:
            start_time -= 1
            sum_time = start_time
            break
        cnt += 1
    if cnt == n:
        break

print(-1 if start_time < 0 else start_time)