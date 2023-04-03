n = int(input())
m = int(input())
answer = []
for i in range(n,m+1):
    l = []
    for j in range(1,i+1):
        if i%j == 0:
            l.append(j)
    if len(l) == 2:
        answer.append(i)
if len(answer) > 0:
    print(sum(answer))
    print(answer[0])
else:
    print(-1)