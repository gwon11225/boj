from sys import stdin
n,m = map(int, stdin.readline().rstrip().split())
dct = {}
for i in range(n):
    word = stdin.readline().rstrip()
    dct[i + 1] = word
    dct[word] = i + 1
for i in range(m):
    word = stdin.readline().rstrip()
    if word.isdigit() == True:
        print(dct[int(word)])
    else:
        print(dct[word])