import sys
arr = [list(sys.stdin.readline().strip().split()) for _ in range(int(sys.stdin.readline()))]
for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])
arr.sort(key=lambda x:(x[0]))
for i in range(len(arr)):
    print(arr[i][0],end=" ")
    print(arr[i][1])