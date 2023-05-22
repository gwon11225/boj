from sys import stdin
while True:
    a = []
    word = stdin.readline().rstrip()
    if word == '.':
        break
    for i in word:
        if i == '(' or i == ')' or i == '[' or i == ']':
            a.append(i)
            if len(a) >= 2:
                if a[-2:] == ['(',')'] or a[-2:] == ['[',']']:
                    a.pop()
                    a.pop()
    print("yes" if len(a) == 0 else "no")