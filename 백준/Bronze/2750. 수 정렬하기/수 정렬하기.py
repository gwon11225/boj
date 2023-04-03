n = int(input())
arr = []
for i in range(n):
    a = int(input())
    arr.append(a)
arr.sort()
for i in range(len(arr)):
    print(arr[i])