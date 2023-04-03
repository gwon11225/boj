while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1,n+1):
        if i == n:
            break
        if n%i == 0:
            arr.append(i)
    if n == sum(arr):
        print(f"{n} = ",end="")
        for i in range(len(arr) - 1):
            print(arr[i],end=" + ")
        print(f"{arr[len(arr)-1]}")
    else:
        print(f"{n} is NOT perfect.")