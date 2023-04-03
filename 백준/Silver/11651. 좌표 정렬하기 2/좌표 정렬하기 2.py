arr = [list(map(int,input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[1],x[0]))
for i in arr:
    for j in i:
        print(j,end=" ")
    print()