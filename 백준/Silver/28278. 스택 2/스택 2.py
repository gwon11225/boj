import sys
arr = []
for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().rstrip()
    if ' ' in cmd:
        cmd = list(map(int, cmd.split()))[1]
        arr.append(cmd)
    else:
        cmd = int(cmd)
        if cmd == 2:
            print(-1 if len(arr) == 0 else arr.pop())
        elif cmd == 3:
            print(len(arr))
        elif cmd == 4:
            print(1 if len(arr) == 0 else 0)
        elif cmd == 5:
            print(-1 if len(arr) == 0 else arr[-1])