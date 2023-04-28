arr = list(map(int,input().split()))
if max(arr) >= sum(arr) - max(arr):
    arr[arr.index(max(arr))] = sum(arr) - max(arr) - 1
print(sum(arr))