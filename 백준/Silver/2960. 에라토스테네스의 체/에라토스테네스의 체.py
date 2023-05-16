n,k = map(int,input().split())
arr = [i for i in range(2,n+1)]
cnt = 0
for i in range(2,n+1):
    for j in range(2,n+1):
        if j%i == 0:
            if arr[j-3] == 0:
                continue
            arr[j-3] = 0
            cnt += 1
        if cnt == k:
            print(j)
            exit()