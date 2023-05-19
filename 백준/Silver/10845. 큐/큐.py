import sys
arr = []
for i in range(int(input())):
    cmd = sys.stdin.readline().rstrip()
    if 'push' in cmd:
        cmd,x = cmd.split()
        x = int(x)
        arr.append(x)
        continue
    if cmd == 'front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    if cmd == 'back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    if cmd == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    if cmd == 'size':
        print(len(arr))
    if cmd == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
            arr.pop(0)