from sys import stdin
n = int(input())
arr = [list(stdin.readline().rstrip().split()) for _ in range(n)]
answer = []
for i in range(n):
    if arr[i][1] == 'enter':
        answer.append(arr[i][0])
    else:
        answer.remove(arr[i][0])
for i in sorted(answer,reverse=True):
    print(i)