a, b, c = map(int, input().split())

arr = []
answer = []

for i in range(1, a + 1):
    for j in range(1, b + 1):
        for k in range(1, c + 1):
            arr.append(i + j + k)

arrset = sorted(list(set(arr)))

for i in arrset:
    answer.append([i, arr.count(i)])

answer.sort(key=lambda x: (-x[1], x[0]))

print(answer[0][0])