n = int(input())
arr = [input() for i in range(n)]

for i in arr:
    ar = []
    for j in list(i):
        if j == ")":
            if len(ar) != 0 and ar[-1] == "(":
                ar.pop()
            else:
                ar.append(j)
        else:
            ar.append(j)
    if len(ar) == 0:
        print("YES")
    else:
        print("NO")