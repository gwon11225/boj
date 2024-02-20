n = int(input())

arr = list(enumerate(map(int, input().split())))

answer = []
position = 0
for i in range(n):
    balloon = arr.pop(position)
    if len(arr) == 0:
        answer.append(balloon[0] + 1)
        break
    
    position -= 1 if balloon[1] >= 0 else 0
    position += balloon[1]
    position %= len(arr)

    answer.append(balloon[0] + 1)

print(*answer)