
while True:
    arr = list(map(int, input().split()))
    if arr.count(arr[0]) == 3:
        break
    m = max(arr)
    arr.remove(m)

    if arr[0] ** 2 + arr[1] ** 2 == m ** 2:
        print("right")
    else:
        print("wrong")