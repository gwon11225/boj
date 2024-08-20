n = int(input())
answer = []

for i in range(1, n + 1):
    ans = list(str(i))

    while '4' in ans or '7' in ans:
        if '4' in ans:
            ans.remove('4')
        if '7' in ans:
            ans.remove('7')

    if len(ans) == 0:
        answer.append(i)
print(answer[-1])