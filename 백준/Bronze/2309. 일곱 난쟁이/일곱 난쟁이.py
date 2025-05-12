arr = [int(input()) for _ in range(9)]
s = sum(arr)
over = s - 100

for i in range(9):
    for j in range(i + 1, 9):
        if i == j:
            continue
        if arr[i] + arr[j] == over:
            a = arr[i]
            b = arr[j]
            arr.remove(a)
            arr.remove(b)
            for d in sorted(arr):
                print(d)
            exit()
