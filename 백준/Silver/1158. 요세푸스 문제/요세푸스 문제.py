a,b = map(int, input().split())

arr = [i for i in range(1, a + 1)]

answer = []

count = 0

for i in range(a):
    for j in range(b):
        if j == b - 1:
            answer.append(arr.pop(0))
        else:
            arr.append(arr.pop(0))
answer = map(str, answer)
print("<" + ", ".join(answer) + ">")