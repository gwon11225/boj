n = int(input())
count = 2
answer = []
while True:
    if n == 1:
        break
    if n%count == 0:
        answer.append(count)
        n /= count
        continue
    count += 1
for i in range(len(answer)):
    print(answer[i])