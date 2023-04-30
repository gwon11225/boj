n,m = map(int,input().split())
arr = list(map(int,input().split()))
answer = []
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or k == i:
                continue
            if arr[i]+arr[j]+arr[k]-m > 0:
                continue
            answer.append(arr[i]+arr[j]+arr[k])
answer.sort()
print(answer[-1])