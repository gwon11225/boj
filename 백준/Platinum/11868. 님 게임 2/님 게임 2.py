n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print("koosaga")
else:
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans ^ arr[i]
    if ans == 0:
        print("cubelover")
    else:
        print("koosaga")