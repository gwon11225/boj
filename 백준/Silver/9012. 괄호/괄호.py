from sys import stdin
n = int(stdin.readline().rstrip())
for i in range(n):
    a = []
    word = stdin.readline().rstrip()
    for j in word:
        a.append(j)
        if len(a) >= 2:
            if a[-2:] == ['(',')']:
                a.pop()
                a.pop()
    print("YES" if len(a) == 0 else "NO")