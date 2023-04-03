import sys
strings = [list(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline()))]
strings.sort()
strings.sort(key=len)
answer = []
for i in range(len(strings)):
    if strings[i] not in answer:
        answer.append(strings[i])
for i in range(len(answer)):
    print(''.join(answer[i]))