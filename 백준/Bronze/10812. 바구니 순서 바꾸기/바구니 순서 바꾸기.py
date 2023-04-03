N,M = map(int,input().split())
arr = [i for i in range(1,N+1)]
for i in range(M):
    answer = []
    first_index,end_index,mid_index = map(int,input().split())
    for j in range(end_index - mid_index + 1):
        answer.append(arr[mid_index - 1 + j])
    for j in range(mid_index - first_index):
        answer.append(arr[first_index - 1 + j])
    for j in range(end_index - first_index + 1):
        arr[j + first_index - 1] = answer[j]
for i in range(N):
    print(arr[i],end=" ")