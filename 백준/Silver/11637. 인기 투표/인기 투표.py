for i in range(int(input())):
    arr = [int(input()) for _ in range(int(input()))]
    m = max(arr)
    cnt = 0
    for i in arr:
        if i == m:
            cnt += 1
    if cnt >= 2:
        print("no winner")
    else:
        if sum(arr) / 2 < m:
            print("majority winner",arr.index(m)+1)
        else:
            print("minority winner",arr.index(m)+1)