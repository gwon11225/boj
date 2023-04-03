m = int(input())
for j in range(m):
    list_1 = list(input().split())
    a = int(list_1[0])
    list_2 = list(list_1[1].strip())
    for i in list_2:
        for _ in range(a):
            print(i,end='')
    print()