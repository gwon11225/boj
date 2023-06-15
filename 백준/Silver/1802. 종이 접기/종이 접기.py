def paper(w):
    if len(w) == 1:
        return True
    mid = len(w)//2
    for i in range(mid):
        if w[i] == w[-i - 1]:
            return False
    return paper(w[:mid])

n = int(input())
for i in range(n):
    print("YES" if paper(input()) else "NO")