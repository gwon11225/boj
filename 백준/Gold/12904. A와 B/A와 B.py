s = list(input())
t = list(input())
while len(s) != len(t):
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if t == s:
        print(1)
        exit()
print(0)