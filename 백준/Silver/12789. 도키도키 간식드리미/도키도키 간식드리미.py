n = int(input())
arr = list(map(int, input().split()))
stop = []

cnt = 1

for i in range(n):
    if cnt in arr:
        while len(arr) != 0 and arr[0] != cnt:
            stop.append(arr.pop(0))
        arr.pop(0)
    else:
        if stop[-1] != cnt:
            print("Sad")
            exit()
        else:
            stop.pop()
    cnt += 1

print("Nice")