def binary(target, arr, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2

    if arr[mid] == target:
        return 1
    
    if arr[mid] > target:
        return binary(target, arr, start, mid - 1)
    if arr[mid] < target:
        return binary(target, arr, mid + 1, end)

n = int(input())
arr = sorted(input().split())

m = int(input())
result = input().split()

for i in result:
    print(binary(i, arr, 0, n - 1))