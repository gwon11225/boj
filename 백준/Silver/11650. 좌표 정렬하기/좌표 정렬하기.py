arr = sorted([list(map(int, input().split())) for _ in range(int(input()))])
for i in arr:
    for j in i:
        print(j,end=" ")
    print()