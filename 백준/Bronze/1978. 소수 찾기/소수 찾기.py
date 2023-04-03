n = int(input())
arr = list(map(int,input().split()))
count = 0
for j in arr:
    answer = []
    for i in range(1,j+1):
        if j%i == 0:
            answer.append(i)
    if len(answer) == 2:
        count += 1
print(count)