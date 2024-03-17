from sys import stdin

n = int(stdin.readline().rstrip())

dancer = ["ChongChong"]

for _ in range(n):
    a,b = stdin.readline().rstrip().split()

    if a in dancer:
        dancer.append(b)
    elif b in dancer:
        dancer.append(a)

print(len(set(dancer)))