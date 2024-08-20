import math

down = int(input())
up = int(input())

minimum = []
answer = 0

for i in range(down, up + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if i == j ** 2:
            answer += i
            minimum.append(i)
if len(minimum) == 0:
    print(-1)
else:
    print(answer)
    print(minimum[0])