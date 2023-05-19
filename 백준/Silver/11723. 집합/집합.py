import sys
n = int(input())
s = 0b0
for i in range(n):
    cmd = sys.stdin.readline().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            s = 0b111111111111111111110
        else:
            s = 0b0
    else:
        cmd, x = cmd
        x = int(x)
        if cmd == 'add':
            s |= (1 << x)
        if cmd == 'remove':
            s &= ~(1<<x)
        if cmd == 'check':
            print(1 if s & (1 << x) else 0)
        if cmd == 'toggle':
            s ^= (1 << x)