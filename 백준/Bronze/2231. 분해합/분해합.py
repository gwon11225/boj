word = input()
n = int(word)
for i in range(n+1):
    w = str(i)
    s = 0
    for j in w:
        s += int(j)
    if i+s == n:
        print(i)
        exit()
print(0)