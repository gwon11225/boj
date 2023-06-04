n = int(input()) + 1
n = list(map(int, list(str(n))))
for i in range(10000):
    for i in range(len(n)//2 + 1):
        if n[i] < n[len(n) - i - 1]:
            n[len(n) - i - 2] += 1
        n[len(n) - i - 1] = n[i]
        for i in range(len(n)-1, -1, -1):
            if n[i] >= 10:
                n[i], n[i - 1] = n[i] % 10, n[i - 1] + n[i]//10
for i in n:
    print(i,end="")