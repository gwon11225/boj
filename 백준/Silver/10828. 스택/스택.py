import sys
n = int(input())
arr = []
for i in range(n):
    word = sys.stdin.readline().rstrip()
    if 'push' in word:
        arr.append(int(word.split()[1]))
    elif word == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif word == 'size':
        print(len(arr))
    elif word == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif word == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop(len(arr) - 1)